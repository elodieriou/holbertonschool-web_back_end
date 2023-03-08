-- Create trigger that decreases the quantity of an item after a new order
CREATE TRIGGER decreases_quantity AFTER INSERT ON orders
FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
