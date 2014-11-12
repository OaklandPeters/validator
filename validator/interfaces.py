"""
All abstract interfaces for the validator ontology.


@todo: Consider the way that message/message_factory should be handled.
    ... if message passed in, then it overrides
@todo: Consider: asserterinterface for AssertKeys for a list of keys. How to make message reflect which ones fail?
    ~ Categories which take an iterable as input.
    ~ IterableCategoryInterface
        --> KeysCategory.Check(subject, ['first', 'last'])
            --> [KeyCategory.Check(subject, term) for term in ['first, 'last']]
"""
import abc

#from . import errors
import errors
    


class CategoryInterface(object):
    """
    Highly generic class object, intended to encompass both Predicate behavior
    and the Ensure behavior.
    """
    __metaclass__ = abc.ABCMeta
    predicate = abc.abstractmethod(lambda cls, subject, *args, **kwargs: NotImplemented)
    exception = abc.abstractproperty()
    message = abc.abstractproperty()
    message_factory = abc.abstractmethod(lambda cls, subject, *args, **kwargs: NotImplemented)
    
    # Mixins
    @classmethod
    def Check(cls, subject, *args, **kwargs):
        return cls.predicate(subject, *args, **kwargs)
    @classmethod
    def Assert(cls, subject, *args, **kwargs):
        if not cls.predicate(subject, *args, **kwargs):
            raise cls.exception(cls.message_factory(subject, *args, **kwargs))
        return subject
    

class EnsurerInterface(object):
    """
    """
    __metaclass__ = abc.ABCMeta

class PredicateInterface(object):
    """
    Predicate classes define all actual function implementations.
        Those implementations are used by child classes - of either
        Assert/Check varieties.
    """
    __metaclass__ = abc.ABCMeta

class AsserterInterface(object):
    """Flow-control logic, and abstract methods for ASSERT variety functions.
    The __call__ provided by this class should trigger the entire logic.
    """
    __metaclass__ = abc.ABCMeta
    predicate = abc.abstractmethod(lambda cls, subject, *args, **kwargs: NotImplemented)
    exception = abc.abstractproperty()
    message = abc.abstractproperty()
    message_factory = abc.abstractmethod(lambda self, subject: NotImplemented)
     
     
class CheckerInterface(object):
    """Flow-control logic AND abstract methods for CHECK variety functions.
    The __call__ provided by this class should trigger the entire logic.
    """
    __metaclass__ = abc.ABCMeta
    predicate = abc.abstractmethod(lambda cls, subject, *args, **kwargs: NotImplemented)


# class SequenceCategoryInterface(object):
#     """
#     CategoryInterface over a Sequence of terms.
#     """
#     __metaclass__ = abc.ABCMeta
#     wrapped_category = abc.abstractproperty()
#     @classmethod


class SequenceCategoryInterface(object):
    """
    CategoryInterface over a Sequence of terms.
    Such as KeysCategory
    
    @cvar singular: CategoryInterface
    @cvar exception: errors.ValidationError
    """
    __metaclass__ = abc.ABCMeta
    
    singular = abc.abstractproperty()
    exception = abc.abstractproperty()
    
    predicate = abc.abstractmethod(lambda cls, *args, **kwargs: NotImplemented)
    passing = abc.abstractmethod(lambda cls, *args, **kwargs: NotImplemented)
    failing = abc.abstractmethod(lambda cls, *args, **kwargs: NotImplemented)
    message_factory = abc.abstractmethod(lambda cls, *args, **kwargs: NotImplemented)

    # Mixins for generic functions
    @classmethod
    def Check(cls, subject, *args, **kwargs):
        return cls.predicate(subject, *args, **kwargs)
    @classmethod
    def Assert(cls, subject, *args, **kwargs):
        if not cls.predicate(subject, *args, **kwargs):
            raise cls.exception(cls.message_factory(subject, *args, **kwargs))
        return subject




# This is **JUST** an idea. Actual implementation must be structured differently
class Assertion(object):
    """This is a stub of structure.
    PROBLEM: this structure only makes sense on an *instanced* class - not one that is callable as class.
    
    @todo: Make this structured to mesh with Validate, IE so that it has a `subject` - the first argument 
    @todo: Consider: having this *only* accept message. With message being generated prior - by calling function.
    
    predicate: function, returning boolean. ~filter-criteria
    """
    
    def __init__(self, predicate, subject,
                 args=tuple(), kwargs=dict(),
                 exception=TypeError, message=None,
                 name="'object'", message_factory=None):
        self.predicate = predicate
        self.subject = subject
        self.args = args
        self.kwargs = kwargs
        self.name = name
        self.exception = exception
        self.message = message # Property. Should do something sophisticated with templates and name
    def __bool__(self):
        return bool(self.predicate(*self.args, **self.kwargs))
    def __call__(self):
        if not bool(self):
            raise self.exception(self.message)