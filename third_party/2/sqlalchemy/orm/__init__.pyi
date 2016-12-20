# Stubs for sqlalchemy.orm (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
## from . import mapper
## from . import interfaces
## from . import deprecated_interfaces
## from . import util
## from . import properties
## from . import relationships
## from . import descriptor_props
from . import session
## from . import scoping
## from . import query
from ..util import langhelpers
## from . import strategy_options

## Mapper = mapper.Mapper
## class_mapper = mapper.class_mapper
## configure_mappers = mapper.configure_mappers
## reconstructor = mapper.reconstructor
## validates = mapper.validates
## EXT_CONTINUE = interfaces.EXT_CONTINUE
## EXT_STOP = interfaces.EXT_STOP
## PropComparator = interfaces.PropComparator
## MapperExtension = deprecated_interfaces.MapperExtension
## SessionExtension = deprecated_interfaces.SessionExtension
## AttributeExtension = deprecated_interfaces.AttributeExtension
## aliased = util.aliased
## join = util.join
## object_mapper = util.object_mapper
## outerjoin = util.outerjoin
## polymorphic_union = util.polymorphic_union
## was_deleted = util.was_deleted
## with_parent = util.with_parent
## with_polymorphic = util.with_polymorphic
## ColumnProperty = properties.ColumnProperty
## RelationshipProperty = relationships.RelationshipProperty
## ComparableProperty = descriptor_props.ComparableProperty
## CompositeProperty = descriptor_props.CompositeProperty
## SynonymProperty = descriptor_props.SynonymProperty
## foreign = relationships.foreign
## remote = relationships.remote
Session = session.Session
object_session = Session.object_session
sessionmaker = session.sessionmaker
## make_transient = session.make_transient
## make_transient_to_detached = session.make_transient_to_detached
## scoped_session = scoping.scoped_session
## AliasOption = query.AliasOption
## Query = query.Query
## Bundle = query.Bundle
public_factory = langhelpers.public_factory

def create_session(bind=..., **kwargs): ...

relationship = ...  # type: Any

def relation(*arg, **kw): ...
def dynamic_loader(argument, **kw): ...

column_property = ...  # type: Any
composite = ...  # type: Any

def backref(name, **kwargs): ...
def deferred(*columns, **kw): ...

synonym = ...  # type: Any
comparable_property = ...  # type: Any

def compile_mappers(): ...
def clear_mappers(): ...

joinedload = ...  # type: Any
joinedload_all = ...  # type: Any
contains_eager = ...  # type: Any
defer = ...  # type: Any
undefer = ...  # type: Any
undefer_group = ...  # type: Any
load_only = ...  # type: Any
lazyload = ...  # type: Any
lazyload_all = ...  # type: Any
subqueryload = ...  # type: Any
subqueryload_all = ...  # type: Any
immediateload = ...  # type: Any
noload = ...  # type: Any
defaultload = ...  # type: Any

## Load = strategy_options.Load

def eagerload(*args, **kwargs): ...
def eagerload_all(*args, **kwargs): ...

contains_alias = ...  # type: Any
