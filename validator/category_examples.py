import errors
import interfaces
#from validator.interfaces import SequenceCategoryInterface

class KeyCategory(interfaces.CategoryInterface):
    @classmethod
    def predicate(cls, subject, key):
        return key in subject
    exception = errors.KeyValidationError
    @classmethod
    def message_factory(cls, subject, key, name="object"):
        return str.format(
            "'{name}' is missing required key '{key}'.",
            name = name,
            key = key
        )
    
    
    @classmethod
    def Check(cls, subject, key):
        return cls.predicate(subject, key)
    @classmethod
    def Assert(cls, subject, key, name="'object'"):
        if not cls.predicate(subject, key):
            raise cls.exception(cls.message_factory(subject, key, name=name))
        return subject


    

class KeysCategory(interfaces.SequenceCategoryInterface):
    """Example of an SequenceCategoryInterface"""
    singular = KeyCategory #@type singular: interfaces.CategoryInterface
    @classmethod
    def predicate(cls, subject, keys):
        return all([
            cls.singular.predicate(subject, key)
            for key in keys
        ])
    @classmethod
    def passing(cls, subject, keys):
        return [
            key for key in keys
            if cls.singular.predicate(subject, key)
        ]
    @classmethod
    def failing(cls, subject, keys):
        return [
            key for key in keys
            if not cls.singular.predicate(subject, key)
        ]
    exception = errors.KeyValidationError
    @classmethod
    def message_factory(cls, subject, keys, name="'object'"):
        return str.format(
            "'{name}' is missing required keys: '{keys}'.",
            name = name,
            keys = ", ".join(cls.failing(subject, keys))
        )
    
#     @classmethod
#     def Assert(cls, subject, keys, name="object"):
#         if not cls.predicate(subject, keys):
#             raise cls.exception(cls.message_factory(subject, keys, name=name))
#         return subject
    
if __name__ == "__main__":
    #KeyCategory.Assert({'first':'a'}, 'first')
    #KeysCategory.Assert({'first':'a'}, ['first','second'])
    print()
    
    
            