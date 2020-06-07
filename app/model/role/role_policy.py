class RolePolicy(object):
    def __init__(self, num_role_policy=None, role_policy_name=None):
        self.__num_role_policy = int(num_role_policy)
        self.__role_policy_name = role_policy_name.value

    @property
    def num_role_policy(self):
        return self.__num_role_policy

    @property
    def role_policy_name(self):
        return self.__role_policy_name

    @num_role_policy.setter
    def num_role_policy(self, value):
        self.__num_role_policy = value

    @role_policy_name.setter
    def role_policy_name(self, value):
        self.__role_policy_name = value

    @num_role_policy.deleter
    def num_role_policy(self):
        del self.__num_role_policy

    @role_policy_name.deleter
    def role_policy_name(self):
        del self.__role_policy_name
