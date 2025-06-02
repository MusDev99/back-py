import os
from flask import render_template, request, redirect, url_for, flash
from .model import Item

# Import the create_app function correctly
try:
    from __init__ import create_app
except ImportError:
    # If running directly, use relative import
    from . import create_app

# Get configuration from environment variable
config_name = os.environ.get('FLASK_ENV', 'development')

# Create the Flask application
app = create_app(config_name)

@app.route('/')
def index():
    """Display all items."""
    items = Item.query.all()
    return render_template('index.html', items=items)

@app.route('/add', methods=['GET', 'POST'])
def add():
    """Add a new item."""
    if request.method == 'POST':
        try:
            name = request.form['name']
            description = request.form['description']
            price = float(request.form.get('price', 0.0))
            
            # Validate input
            if not name.strip():
                flash('Item name is required.', 'error')
                return render_template('add.html')
            
            if price < 0:
                flash('Price cannot be negative.', 'error')
                return render_template('add.html')
            
            # Create new item
            Item.create_item(name=name, description=description, price=price)
            flash('Item added successfully!', 'success')
            return redirect(url_for('index'))  # Fixed: removed 'items.' prefix
            
        except ValueError:
            flash('Invalid price format.', 'error')
            return render_template('add.html')
        except Exception as e:
            flash(f'Error adding item: {str(e)}', 'error')
            return render_template('add.html')
    
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    """Edit an existing item."""
    item = Item.query.get_or_404(id)
    
    if request.method == 'POST':
        try:
            name = request.form['name']
            description = request.form['description']
            price = float(request.form.get('price', 0.0))
            
            # Validate input
            if not name.strip():
                flash('Item name is required.', 'error')
                return render_template('edit.html', item=item)
            
            if price < 0:
                flash('Price cannot be negative.', 'error')
                return render_template('edit.html', item=item)
            
            # Update item
            item.update_item(name=name, description=description, price=price)
            flash('Item updated successfully!', 'success')
            return redirect(url_for('index'))  # Fixed: removed 'items.' prefix
            
        except ValueError:
            flash('Invalid price format.', 'error')
            return render_template('edit.html', item=item)
        except Exception as e:
            flash(f'Error updating item: {str(e)}', 'error')
            return render_template('edit.html', item=item)
    
    return render_template('edit.html', item=item)

@app.route('/delete/<int:id>')
def delete(id):
    """Delete an item."""
    item = Item.query.get_or_404(id)
    
    try:
        item_name = item.name
        item.delete_item()
        flash(f'Item "{item_name}" deleted successfully!', 'success')
    except Exception as e:
        flash(f'Error deleting item: {str(e)}', 'error')
    
    return redirect(url_for('index'))  # Fixed: removed 'items.' prefix

if __name__ == '__main__':
    app.run(debug=True)