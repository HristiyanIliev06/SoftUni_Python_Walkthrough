from unittest import TestCase, main
from project.social_media import SocialMedia


class TestSocialMediaClass(TestCase):
    def setUp(self):
        self.part = SocialMedia('FeltStarling', 'Instagram', 500000, 'coding')

    def test_social_media_structure(self):
        self.assertEqual(SocialMedia.__base__.__name__, "object")
        self.assertTrue(hasattr(SocialMedia, "_validate_and_set_platform"))
        self.assertTrue(hasattr(SocialMedia, "create_post"))
        self.assertTrue(hasattr(SocialMedia, "like_post"))
        self.assertTrue(hasattr(SocialMedia, "comment_on_post"))

        self.assertTrue(isinstance(getattr(SocialMedia, "platform"), property))
        self.assertTrue(isinstance(getattr(SocialMedia, "followers"), property))

    def test_initialization(self):
        part = SocialMedia('FeltStarling', 'Instagram', 500000, 'coding')
        self.assertEqual(part._username, 'FeltStarling')
        self.assertEqual(part._platform, 'Instagram')
        self.assertEqual(part.followers, 500000)
        self.assertEqual(part._content_type, 'coding')
        self.assertEqual(part._posts, [])

    def test__validate_and_set_platform_valid(self):
        valid_platforms = ['Instagram', 'YouTube', 'Twitter']
        for platform in valid_platforms:
            with self.subTest(platform=platform):
                self.part.platform = platform
                self.assertEqual(self.part.platform, platform)

    def test__validate_and_set_platform_invalid(self):
        valid_platforms = ['Instagram', 'YouTube', 'Twitter']
        invalid_platform = 'InvalidPlatform'
        with self.assertRaises(ValueError) as context:
            self.part.platform = invalid_platform
        self.assertEqual(str(context.exception), f"Platform should be one of {valid_platforms}")

    def test_create_post(self):
        '''software1 = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}
        software2 = {'name': 'Software2', 'capacity_consumption': 40, 'memory_consumption': 70}
        self.part.installed_software = [software1, software2]
        self.assertEqual(self.part.get_used_capacity(), 70)'''
        post_content = 'design'
        new_post = {'content': post_content, 'likes': 0, 'comments': []}
        self.part._posts.append(new_post)
        message = f"New {self.part._content_type} post created by {self.part._username} on {self.part._platform}."
        self.assertEqual(self.part._posts, {'content': 'design', 'likes': 0, 'comments': []})
        self.assertEqual(message, f"New coding post created by FeltStarling on Instagram.")

    def test_get_available_capacity(self):
        self.part.installed_software = [{'capacity_consumption': 30}]
        self.assertEqual(self.part.get_available_capacity(), 70)

    def test_get_used_memory(self):
        software1 = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}
        software2 = {'name': 'Software2', 'capacity_consumption': 40, 'memory_consumption': 70}
        self.part.installed_software = [software1, software2]
        self.assertEqual(self.part.get_used_memory(), 120)

    def test_get_available_memory(self):
        self.part.installed_software = [{'memory_consumption': 30}]
        self.assertEqual(self.part.get_available_memory(), 170)

    def test_install_software_success(self):
        software = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}
        result = self.part.install_software(software)
        self.assertEqual(result, f"Software '{software['name']}' successfully installed on {self.part.category} part.")
        self.assertEqual(self.part.installed_software, [software])

    def test_install_software_exact_capacity_memory(self):
        software = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}
        self.part.installed_software = []
        self.part.capacity = software['capacity_consumption']
        self.part.memory = software['memory_consumption']

        result = self.part.install_software(software)

        expected_message = f"Software '{software['name']}' successfully installed on {self.part.category} part."
        self.assertEqual(result, expected_message)
        self.assertEqual(self.part.installed_software, [software])

    def test_install_software_memory_condition_only(self):
        software = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}
        self.part.installed_software = []
        self.part.capacity = software['capacity_consumption'] - 5
        self.part.memory = software['memory_consumption'] + 10

        result = self.part.install_software(software)
        expected_message = f"Software '{software['name']}' cannot be installed on {self.part.category} part."
        self.assertEqual(result, expected_message)
        self.assertEqual(self.part.installed_software, [])

    def test_install_software_capacity_condition_only(self):
        software = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}
        self.part.installed_software = []
        self.part.capacity = software['capacity_consumption'] + 10
        self.part.memory = software['memory_consumption'] - 5

        result = self.part.install_software(software)
        expected_message = f"Software '{software['name']}' cannot be installed on {self.part.category} part."
        self.assertEqual(result, expected_message)
        self.assertEqual(self.part.installed_software, [])

    def test_install_software_failure(self):
        software = {'name': 'Software1', 'capacity_consumption': 150, 'memory_consumption': 250}
        result = self.part.install_software(software)
        expected_message = f"Software '{software['name']}' cannot be installed on {self.part.category} part."
        self.assertEqual(result, expected_message)
        self.assertEqual(self.part.installed_software, [])


if __name__ == '__main__':
    main()