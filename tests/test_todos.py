import unittest
import app


class TestStores(unittest.TestCase):
    def setUp(self):
        app.app.testing = True
        app.app.config['FLASK_ENV'] = 'development'
        self.app = app.app.test_client()

        with app.app.app_context():
            app.app.testing = False
            app.app.config['FLASK_ENV'] = 'production'

    def test_create_todo(self):
        rv = self.app.post('/store', data={'name': 'store2'})
        dados = {'name': 'store2'}
        self.assertDictContainsSubset(dados, rv.get_json())

    def test_get_store(self):
        rv = self.app.get('/store')
        dados = {'name': 'store1'}
        self.assertIn(bytes(dados['name'], 'utf-8'), rv.data)


if __name__ == '__main__':
    unittest.main()
