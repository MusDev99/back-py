from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()

class Item(db.Model):
    """Item model for storing product information."""
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False, default=0.0)

    def __repr__(self):
        return f'<Item {self.name}>'
    
    def to_dict(self):
        """Convert item to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price
        }
    
    @classmethod
    def create_item(cls, name, description, price):
        """Create a new item and save to database."""
        new_item = cls(name=name, description=description, price=price)
        db.session.add(new_item)
        db.session.commit()
        return new_item
    
    def update_item(self, name, description, price):
        """Update existing item."""
        self.name = name
        self.description = description
        self.price = price
        db.session.commit()
    
    def delete_item(self):
        """Delete item from database."""
        db.session.delete(self)
        db.session.commit()