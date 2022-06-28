import unittest
from employee_management import Employee, Post, Manager

class TestManagementSystem(unittest.TestCase):
    def test_employee_init(self):
        employee = Employee("Madeline", "Boudreau")
        self.assertIn(employee, employee.all_)
        
    def test_create_manager(self):
        employee = Employee("Derek", "Hawkins")
        manager = Manager("Ripal", "Coding_Temple")
        self.assertFalse(manager.employees)

    def test_add_employee(self):
        employee1 = Employee("Madeline", "Boudreau")
        manager = Manager("Lucas", "Lang")
        self.assertNotIn(employee1 ,manager.employees)

    def test_create_post(self):
        # tests if the created post reads out the correct body
        employee = Employee("Madeline", "Boudreau")
        post_body = "This is a test."
        new_post = Post(post_body, employee.email)
        self.assertIn(new_post.body, "This is a test.")

        # tests if creating a post attaches it to the correct employees post list
        employee.create_post()
        self.assertTrue(employee.posts)

    def test_show_post(self):
        # tests if an uploaded post is added to the company post feed
        employee = Employee("Madeline", "Boudreau")
        post_body = "This is a test."
        new_post = Post(post_body, employee.email)
        self.assertIn(new_post, Post.all_)

if __name__ == '__main__':
        unittest.main()
