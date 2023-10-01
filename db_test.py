import unittest
from peewee import SqliteDatabase
from db import ProductModel, create_product, get_product_by_id, update_product, delete_product

# Use an in-memory SQLite database for testing
test_db = SqliteDatabase(':memory:')


class TestProductModel(unittest.TestCase):
    def setUp(self):
        # Connect to the in-memory database and create tables
        test_db.connect()
        test_db.create_tables([ProductModel], safe=True)

    def tearDown(self):
        # Close the database connection
        test_db.close()

    def test_create_product(self):
        product = create_product("Test Product", 50)
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.price, 50)

    def test_get_product_by_id(self):
        # Create a test product
        test_product = create_product("Test Product", 50)
        product = get_product_by_id(test_product.id)
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.price, 50)

    def test_update_product(self):
        # Create a test product
        test_product = create_product("Test Product", 50)
        # Update the product
        updated_product = update_product(test_product.id, name="Updated Product", price=75)
        self.assertEqual(updated_product.name, "Updated Product")
        self.assertEqual(updated_product.price, 75)

    def test_delete_product(self):
        # Create a test product
        test_product = create_product("Test Product", 50)
        # Delete the product
        delete_success = delete_product(test_product.id)
        self.assertTrue(delete_success)
        # Attempt to get the deleted product should return None
        product = get_product_by_id(test_product.id)
        self.assertIsNone(product)


if __name__ == "__main__":
    unittest.main()
