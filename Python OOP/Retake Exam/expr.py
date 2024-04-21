'''d = {'a':1}
print(d.get('a', "XXXXXXXXXXXXXXXXXXXX"))'''

class Restaurant:

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.waiters = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or not value.strip():
            raise ValueError("Invalid name!")
        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Invalid capacity!")
        self.__capacity = value

    def get_waiters(self, min_earnings=None, max_earnings=None):
        filtered_waiters = [waiter for waiter in self.waiters
                            if (min_earnings is None or waiter.get('total_earnings', 0) >= min_earnings) and
                            (max_earnings is None or waiter.get('total_earnings', 0) <= max_earnings)]
        return filtered_waiters

    def add_waiter(self, waiter_name):
        if len(self.waiters) == self.capacity:
            return "No more places!"

        if waiter_name in (existing_waiter['name'] for existing_waiter in self.waiters):
            return f"The waiter {waiter_name} already exists!"

        new_waiter = {'name': waiter_name}
        self.waiters.append(new_waiter)
        return f"The waiter {waiter_name} has been added."

    def remove_waiter(self, waiter_name):
        for waiter in self.waiters:
            if waiter['name'] == waiter_name:
                self.waiters.remove(waiter)
                return f"The waiter {waiter_name} has been removed."
        return f"No waiter found with the name {waiter_name}."

    def get_total_earnings(self):
        return sum(waiter.get('total_earnings', 0) for waiter in self.waiters)




from unittest import TestCase, main


class TestClimbingRobot(TestCase):
    #ALLOWED_CATEGORIES = ['Mountain', 'Alpine', 'Indoor', 'Bouldering']

    def setUp(self):
        self.restaurant = Restaurant(
            "Escape",
            100
        )

        '''self.robot_with_software = ClimbingRobot(
            "Mountain",
            "Helper",
            100,
            200,
        )'''

        '''self.robot_with_software.installed_software = [
            {"name": "PyCharm", "capacity_consumption": 50, "memory_consumption": 49},
            {"name": "CLion", "capacity_consumption": 49, "memory_consumption": 51}
        ]'''

    def test_correct__init__(self):
        self.assertEqual("Escape", self.restaurant.name)
        self.assertEqual(100, self.restaurant.capacity)
        self.assertEqual([], self.restaurant.waiters)

    def test_create_restaurant_with_invalid_name_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.restaurant.name = ""

        self.assertEqual("Invalid name!", str(ve.exception))
        
    def test_create_restaurant_with_invalid_capacity_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.restaurant.capacity = -1

        self.assertEqual("Invalid capacity!", str(ve.exception))

    
    def test_add_waiter_unsuccessful_due_to_existing_name(self):
        self.restaurant.waiters = [{'name': 'Pesho'}, {'name': 'Gosho'}, {'name': 'Emrah'}]
         
        actual = "The waiter Emrah already exists!"
        
        self.assertEqual(self.restaurant.add_waiter("Emrah"), actual)
    
    def test_add_waiter_successful(self):
        self.restaurant.waiters = [{'name': 'Pesho'}, {'name': 'Gosho'}, {'name': 'Emrah'}]
         
        actual_message = "The waiter Misho has been added."
        
        self.assertEqual(self.restaurant.add_waiter("Misho"), actual_message) 
        self.assertEqual(self.restaurant.waiters, [{'name': 'Pesho'}, {'name': 'Gosho'}, {'name': 'Emrah'}, {'name': 'Misho'}])
        
    def test_remove_waiter_unsuccessful_because_not_found(self):
        self.restaurant.waiters = [{'name': 'Pesho'}, {'name': 'Gosho'}, {'name': 'Emrah'}]
        
        actual = f"No waiter found with the name Misho."

        self.assertEqual(self.restaurant.remove_waiter("Misho"), actual)
        
    def test_remove_waiter_successful(self):
        self.restaurant.waiters = [{'name': 'Pesho'}, {'name': 'Gosho'}, {'name': 'Emrah'}]
        
        actual = "The waiter Gosho has been removed."
        
        
        self.assertEqual(self.restaurant.remove_waiter("Gosho"), actual)
        self.assertEqual(self.restaurant.waiters, [{'name': 'Pesho'}, {'name': 'Emrah'}]) 
    
    def test_get_total_earnings(self):
        self.restaurant.waiters = [{'name': 'Pesho', 'total_earnings': 5000}, 
                                   {'name': 'Gosho', 'total_earnings': 5000}, 
                                   {'name': 'Emrah', 'total_earnings': 5000}
        ]

        actual = 15000.0

        self.assertEqual(self.restaurant.get_total_earnings(), actual)       
'''   def test_add_waiter_unsuccessful_due_to_existing_name(self):
        self.restaurant.waiters = ['Pesho', 'Gosho', 'Emrah']
        self.restaurant.capacity = 4
        
        actual = "The waiter Emrah already exists!"
        
        self.assertEqual(self.restaurant.add_waiter("Emrah"), actual)
        
        
    def test_get_waiters(self):
        min_earnings=None
        max_earnings=None
        expected_result = sum(s['capacity_consumption'] for s in self.robot_with_software.installed_software)
        result = self.robot_with_software.get_used_capacity()

        self.assertEqual(expected_result, result)'''

'''
    def test_get_available_capacity_expect_success(self):
        expected_result = self.robot.capacity - sum(s['capacity_consumption'] for s in self.robot_with_software.installed_software)
        result = self.robot_with_software.get_available_capacity()

        self.assertEqual(result, expected_result)

    def test_get_used_memory_expect_success(self):
        expected_result = sum(s['memory_consumption'] for s in self.robot_with_software.installed_software)
        result = self.robot_with_software.get_used_memory()

        self.assertEqual(expected_result, result)

    def test_get_available_memory_expect_success(self):
        expected_result = self.robot.memory - sum(s['memory_consumption'] for s in self.robot_with_software.installed_software)
        result = self.robot_with_software.get_available_memory()

        self.assertEqual(result, expected_result)

    def test_install_software_with_max_equal_values_expect_success(self):
        result = self.robot.install_software(
            {"name": "PyCharm", "capacity_consumption": 100, "memory_consumption": 200},
        )

        self.assertEqual(
            f"Software 'PyCharm' successfully installed on Mountain part.",
            result
        )

        self.assertEqual(
            self.robot.installed_software,
            [{"name": "PyCharm", "capacity_consumption": 100, "memory_consumption": 200}]
        )

    def test_install_software_with_less_than_max_values_expect_success(self):
        result = self.robot.install_software(
            {"name": "PyCharm", "capacity_consumption": 10, "memory_consumption": 20},
        )

        self.assertEqual(
            f"Software 'PyCharm' successfully installed on Mountain part.",
            result
        )

        self.assertEqual(
            self.robot.installed_software,
            [{"name": "PyCharm", "capacity_consumption": 10, "memory_consumption": 20}]
        )

    def test_install_software_with_one_value_greater_than_max_values_return_error_message(self):
        result = self.robot.install_software(
            {"name": "PyCharm", "capacity_consumption": 10, "memory_consumption": 2000},
        )

        self.assertEqual(
            f"Software 'PyCharm' cannot be installed on Mountain part.",
            result
        )

        self.assertEqual(
            self.robot.installed_software,
            []
        )

    def test_install_software_with_both_value_greater_than_max_values_return_error_message(self):
        result = self.robot_with_software.install_software(
            {"name": "PyCharm", "capacity_consumption": 49, "memory_consumption": 50},
        )

        self.assertEqual(
            f"Software 'PyCharm' cannot be installed on Mountain part.",
            result
        )

        self.assertEqual(
            self.robot.installed_software,
            []
        )'''


if __name__ == "__main__":
    main()

