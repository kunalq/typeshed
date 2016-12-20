# Stubs for sqlalchemy.dialects.mysql.base (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from ... import sql
from ... import engine
from ... import util
from ... import types

sqltypes = sql.sqltypes
## compiler = sql.compiler
## reflection = engine.reflection
## default = engine.default
## topological = util.topological
DATE = types.DATE
BOOLEAN = types.BOOLEAN
BLOB = types.BLOB
BINARY = types.BINARY
VARBINARY = types.VARBINARY

RESERVED_WORDS = ...  # type: Any
AUTOCOMMIT_RE = ...  # type: Any
SET_RE = ...  # type: Any

class _NumericType:
    unsigned = ...  # type: Any
    zerofill = ...  # type: Any
    def __init__(self, unsigned=..., zerofill=..., **kw) -> None: ...

class _FloatType(_NumericType,
                 ## sqltypes.Float
                 ):
    scale = ...  # type: Any
    def __init__(self, precision=..., scale=..., asdecimal=..., **kw) -> None: ...

class _IntegerType(_NumericType,
                   ## sqltypes.Integer
                   ):
    display_width = ...  # type: Any
    def __init__(self, display_width=..., **kw) -> None: ...

class _StringType(object,
                  ## sqltypes.String
                  ):
    charset = ...  # type: Any
    ascii = ...  # type: Any
    unicode = ...  # type: Any
    binary = ...  # type: Any
    national = ...  # type: Any
    def __init__(self, charset=..., collation=..., ascii=..., binary=..., unicode=..., national=..., **kw) -> None: ...

class _MatchType(object,
                 ## sqltypes.Float,
                 ## sqltypes.MatchType
                 ):
    def __init__(self, **kw) -> None: ...

class NUMERIC(_NumericType,
              ## sqltypes.NUMERIC
              ):
    __visit_name__ = ...  # type: Any
    def __init__(self, precision=..., scale=..., asdecimal=..., **kw) -> None: ...

class DECIMAL(_NumericType,
              ## sqltypes.DECIMAL
              ):
    __visit_name__ = ...  # type: Any
    def __init__(self, precision=..., scale=..., asdecimal=..., **kw) -> None: ...

class DOUBLE(_FloatType):
    __visit_name__ = ...  # type: Any
    def __init__(self, precision=..., scale=..., asdecimal=..., **kw) -> None: ...

class REAL(_FloatType,
           ## sqltypes.REAL
           ):
    __visit_name__ = ...  # type: Any
    def __init__(self, precision=..., scale=..., asdecimal=..., **kw) -> None: ...

class FLOAT(_FloatType,
            ## sqltypes.FLOAT
            ):
    __visit_name__ = ...  # type: Any
    def __init__(self, precision=..., scale=..., asdecimal=..., **kw) -> None: ...
    def bind_processor(self, dialect): ...

class INTEGER(_IntegerType,
              ## sqltypes.INTEGER
              ):
    __visit_name__ = ...  # type: Any
    def __init__(self, display_width=..., **kw) -> None: ...

class BIGINT(_IntegerType,
             ## sqltypes.BIGINT
             ):
    __visit_name__ = ...  # type: Any
    def __init__(self, display_width=..., **kw) -> None: ...

class MEDIUMINT(_IntegerType):
    __visit_name__ = ...  # type: Any
    def __init__(self, display_width=..., **kw) -> None: ...

class TINYINT(_IntegerType):
    __visit_name__ = ...  # type: Any
    def __init__(self, display_width=..., **kw) -> None: ...

class SMALLINT(_IntegerType,
               ## sqltypes.SMALLINT
               ):
    __visit_name__ = ...  # type: Any
    def __init__(self, display_width=..., **kw) -> None: ...

class BIT(object,
          ## sqltypes.TypeEngine
          ):
    __visit_name__ = ...  # type: Any
    length = ...  # type: Any
    def __init__(self, length=...) -> None: ...
    def result_processor(self, dialect, coltype): ...

class TIME(object,
           ## sqltypes.TIME
           ):
    __visit_name__ = ...  # type: Any
    fsp = ...  # type: Any
    def __init__(self, timezone=..., fsp=...) -> None: ...
    def result_processor(self, dialect, coltype): ...

class TIMESTAMP(object,
                ## sqltypes.TIMESTAMP
                ):
    __visit_name__ = ...  # type: Any
    fsp = ...  # type: Any
    def __init__(self, timezone=..., fsp=...) -> None: ...

class DATETIME(object,
               ## sqltypes.DATETIME
               ):
    __visit_name__ = ...  # type: Any
    fsp = ...  # type: Any
    def __init__(self, timezone=..., fsp=...) -> None: ...

class YEAR(object,
           ## sqltypes.TypeEngine
           ):
    __visit_name__ = ...  # type: Any
    display_width = ...  # type: Any
    def __init__(self, display_width=...) -> None: ...

class TEXT(_StringType,
           ## sqltypes.TEXT
           ):
    __visit_name__ = ...  # type: Any
    def __init__(self, length=..., **kw) -> None: ...

class TINYTEXT(_StringType):
    __visit_name__ = ...  # type: Any
    def __init__(self, **kwargs) -> None: ...

class MEDIUMTEXT(_StringType):
    __visit_name__ = ...  # type: Any
    def __init__(self, **kwargs) -> None: ...

class LONGTEXT(_StringType):
    __visit_name__ = ...  # type: Any
    def __init__(self, **kwargs) -> None: ...

class VARCHAR(_StringType,
              ## sqltypes.VARCHAR
              ):
    __visit_name__ = ...  # type: Any
    def __init__(self, length=..., **kwargs) -> None: ...

class CHAR(_StringType,
           ## sqltypes.CHAR
           ):
    __visit_name__ = ...  # type: Any
    def __init__(self, length=..., **kwargs) -> None: ...

class NVARCHAR(_StringType,
               ## sqltypes.NVARCHAR
               ):
    __visit_name__ = ...  # type: Any
    def __init__(self, length=..., **kwargs) -> None: ...

class NCHAR(_StringType,
            ## sqltypes.NCHAR
            ):
    __visit_name__ = ...  # type: Any
    def __init__(self, length=..., **kwargs) -> None: ...

class TINYBLOB(object,
               ## sqltypes._Binary
               ):
    __visit_name__ = ...  # type: Any

class MEDIUMBLOB(object,
                 ## sqltypes._Binary
                 ):
    __visit_name__ = ...  # type: Any

class LONGBLOB(object,
               ## sqltypes._Binary
               ):
    __visit_name__ = ...  # type: Any

class _EnumeratedValues(_StringType): ...

class ENUM(  # sqltypes.Enum,
           _EnumeratedValues
           ):
    __visit_name__ = ...  # type: Any
    strict = ...  # type: Any
    def __init__(self, *enums, **kw) -> None: ...
    def bind_processor(self, dialect): ...
    def adapt(self, cls, **kw): ...

class SET(_EnumeratedValues):
    __visit_name__ = ...  # type: Any
    retrieve_as_bitwise = ...  # type: Any
    values = ...  # type: Any
    def __init__(self, *values, **kw) -> None: ...
    def column_expression(self, colexpr): ...
    def result_processor(self, dialect, coltype): ...
    def bind_processor(self, dialect): ...
    def adapt(self, impltype, **kw): ...

MSTime = ...  # type: Any
MSSet = ...  # type: Any
MSEnum = ...  # type: Any
MSLongBlob = ...  # type: Any
MSMediumBlob = ...  # type: Any
MSTinyBlob = ...  # type: Any
MSBlob = ...  # type: Any
MSBinary = ...  # type: Any
MSVarBinary = ...  # type: Any
MSNChar = ...  # type: Any
MSNVarChar = ...  # type: Any
MSChar = ...  # type: Any
MSString = ...  # type: Any
MSLongText = ...  # type: Any
MSMediumText = ...  # type: Any
MSTinyText = ...  # type: Any
MSText = ...  # type: Any
MSYear = ...  # type: Any
MSTimeStamp = ...  # type: Any
MSBit = ...  # type: Any
MSSmallInteger = ...  # type: Any
MSTinyInteger = ...  # type: Any
MSMediumInteger = ...  # type: Any
MSBigInteger = ...  # type: Any
MSNumeric = ...  # type: Any
MSDecimal = ...  # type: Any
MSDouble = ...  # type: Any
MSReal = ...  # type: Any
MSFloat = ...  # type: Any
MSInteger = ...  # type: Any
colspecs = ...  # type: Any
ischema_names = ...  # type: Any

class MySQLExecutionContext(object,
                            ## default.DefaultExecutionContext
                            ):
    def should_autocommit_text(self, statement): ...

class MySQLCompiler(object,
                    ## compiler.SQLCompiler
                    ):
    render_table_with_column_in_update_from = ...  # type: Any
    extract_map = ...  # type: Any
    def visit_random_func(self, fn, **kw): ...
    def visit_utc_timestamp_func(self, fn, **kw): ...
    def visit_sysdate_func(self, fn, **kw): ...
    def visit_concat_op_binary(self, binary, operator, **kw): ...
    def visit_match_op_binary(self, binary, operator, **kw): ...
    def get_from_hint_text(self, table, text): ...
    def visit_typeclause(self, typeclause, type_=...): ...
    def visit_cast(self, cast, **kwargs): ...
    def render_literal_value(self, value, type_): ...
    def visit_true(self, element, **kw): ...
    def visit_false(self, element, **kw): ...
    def get_select_precolumns(self, select, **kw): ...
    def visit_join(self, join, asfrom=..., **kwargs): ...
    def for_update_clause(self, select, **kw): ...
    def limit_clause(self, select, **kw): ...
    def update_limit_clause(self, update_stmt): ...
    def update_tables_clause(self, update_stmt, from_table, extra_froms, **kw): ...
    def update_from_clause(self, update_stmt, from_table, extra_froms, from_hints, **kw): ...

class MySQLDDLCompiler(object,
                       ## compiler.DDLCompiler
                       ):
    def create_table_constraints(self, table, **kw): ...
    def get_column_specification(self, column, **kw): ...
    def post_create_table(self, table): ...
    def visit_create_index(self, create): ...
    def visit_primary_key_constraint(self, constraint): ...
    def visit_drop_index(self, drop): ...
    def visit_drop_constraint(self, drop): ...
    def define_constraint_match(self, constraint): ...

class MySQLTypeCompiler(object,
                        ## compiler.GenericTypeCompiler
                        ):
    def visit_NUMERIC(self, type_, **kw): ...
    def visit_DECIMAL(self, type_, **kw): ...
    def visit_DOUBLE(self, type_, **kw): ...
    def visit_REAL(self, type_, **kw): ...
    def visit_FLOAT(self, type_, **kw): ...
    def visit_INTEGER(self, type_, **kw): ...
    def visit_BIGINT(self, type_, **kw): ...
    def visit_MEDIUMINT(self, type_, **kw): ...
    def visit_TINYINT(self, type_, **kw): ...
    def visit_SMALLINT(self, type_, **kw): ...
    def visit_BIT(self, type_, **kw): ...
    def visit_DATETIME(self, type_, **kw): ...
    def visit_DATE(self, type_, **kw): ...
    def visit_TIME(self, type_, **kw): ...
    def visit_TIMESTAMP(self, type_, **kw): ...
    def visit_YEAR(self, type_, **kw): ...
    def visit_TEXT(self, type_, **kw): ...
    def visit_TINYTEXT(self, type_, **kw): ...
    def visit_MEDIUMTEXT(self, type_, **kw): ...
    def visit_LONGTEXT(self, type_, **kw): ...
    def visit_VARCHAR(self, type_, **kw): ...
    def visit_CHAR(self, type_, **kw): ...
    def visit_NVARCHAR(self, type_, **kw): ...
    def visit_NCHAR(self, type_, **kw): ...
    def visit_VARBINARY(self, type_, **kw): ...
    def visit_large_binary(self, type_, **kw): ...
    def visit_enum(self, type_, **kw): ...
    def visit_BLOB(self, type_, **kw): ...
    def visit_TINYBLOB(self, type_, **kw): ...
    def visit_MEDIUMBLOB(self, type_, **kw): ...
    def visit_LONGBLOB(self, type_, **kw): ...
    def visit_ENUM(self, type_, **kw): ...
    def visit_SET(self, type_, **kw): ...
    def visit_BOOLEAN(self, type, **kw): ...

class MySQLIdentifierPreparer(object,
                              ## compiler.IdentifierPreparer
                              ):
    reserved_words = ...  # type: Any
    def __init__(self, dialect, server_ansiquotes=..., **kw) -> None: ...

class MySQLDialect(object,
                   ## default.DefaultDialect
                   ):
    name = ...  # type: Any
    supports_alter = ...  # type: Any
    supports_native_boolean = ...  # type: Any
    max_identifier_length = ...  # type: Any
    max_index_name_length = ...  # type: Any
    supports_native_enum = ...  # type: Any
    supports_sane_rowcount = ...  # type: Any
    supports_sane_multi_rowcount = ...  # type: Any
    supports_multivalues_insert = ...  # type: Any
    default_paramstyle = ...  # type: Any
    colspecs = ...  # type: Any
    statement_compiler = ...  # type: Any
    ddl_compiler = ...  # type: Any
    type_compiler = ...  # type: Any
    ischema_names = ...  # type: Any
    preparer = ...  # type: Any
    construct_arguments = ...  # type: Any
    isolation_level = ...  # type: Any
    def __init__(self, isolation_level=..., **kwargs) -> None: ...
    def on_connect(self): ...
    def set_isolation_level(self, connection, level): ...
    def get_isolation_level(self, connection): ...
    def do_commit(self, dbapi_connection): ...
    def do_rollback(self, dbapi_connection): ...
    def do_begin_twophase(self, connection, xid): ...
    def do_prepare_twophase(self, connection, xid): ...
    def do_rollback_twophase(self, connection, xid, is_prepared=..., recover=...): ...
    def do_commit_twophase(self, connection, xid, is_prepared=..., recover=...): ...
    def do_recover_twophase(self, connection): ...
    def is_disconnect(self, e, connection, cursor): ...
    def has_table(self, connection, table_name, schema=...): ...
    identifier_preparer = ...  # type: Any
    def initialize(self, connection): ...
    def get_schema_names(self, connection, **kw): ...
    def get_table_names(self, connection, schema=..., **kw): ...
    def get_view_names(self, connection, schema=..., **kw): ...
    def get_table_options(self, connection, table_name, schema=..., **kw): ...
    def get_columns(self, connection, table_name, schema=..., **kw): ...
    def get_pk_constraint(self, connection, table_name, schema=..., **kw): ...
    def get_foreign_keys(self, connection, table_name, schema=..., **kw): ...
    def get_indexes(self, connection, table_name, schema=..., **kw): ...
    def get_unique_constraints(self, connection, table_name, schema=..., **kw): ...
    def get_view_definition(self, connection, view_name, schema=..., **kw): ...

class ReflectedState:
    columns = ...  # type: Any
    table_options = ...  # type: Any
    table_name = ...  # type: Any
    keys = ...  # type: Any
    constraints = ...  # type: Any
    def __init__(self) -> None: ...

class MySQLTableDefinitionParser:
    dialect = ...  # type: Any
    preparer = ...  # type: Any
    def __init__(self, dialect, preparer) -> None: ...
    def parse(self, show_create, charset): ...

class _DecodingRowProxy:
    rowproxy = ...  # type: Any
    charset = ...  # type: Any
    def __init__(self, rowproxy, charset) -> None: ...
    def __getitem__(self, index): ...
    def __getattr__(self, attr): ...
