Module(body=[Import(names=[alias(name='os')]), ImportFrom(module='pathlib', names=[alias(name='Path')], level=0), Import(names=[alias(name='shutil')]), Import(names=[alias(name='sys')]), Import(names=[alias(name='toml')]), ImportFrom(module='sphinx.application', names=[alias(name='Sphinx')], level=0), ImportFrom(module='sphinx.ext.autosummary', names=[alias(name='Autosummary')], level=0), Assign(targets=[Name(id='SOURCE_PATH', ctx=Store())], value=Call(func=Name(id='Path', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='os', ctx=Load()), attr='path', ctx=Load()), attr='dirname', ctx=Load()), args=[Name(id='__file__', ctx=Load())], keywords=[])], keywords=[])), Assign(targets=[Name(id='PROJECT_PATH', ctx=Store())], value=Call(func=Attribute(value=Name(id='SOURCE_PATH', ctx=Load()), attr='joinpath', ctx=Load()), args=[Constant(value='../..')], keywords=[])), Assign(targets=[Name(id='COMMIT_SHORT_SHA', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='os', ctx=Load()), attr='environ', ctx=Load()), attr='get', ctx=Load()), args=[Constant(value='CI_COMMIT_SHORT_SHA'), Constant(value=None)], keywords=[])), Assign(targets=[Name(id='WORKFLOW_NAME', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='os', ctx=Load()), attr='environ', ctx=Load()), attr='get', ctx=Load()), args=[Constant(value='WORKFLOW_NAME'), Constant(value=None)], keywords=[])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='sys', ctx=Load()), attr='path', ctx=Load()), attr='insert', ctx=Load()), args=[Constant(value=0), Call(func=Name(id='str', ctx=Load()), args=[Name(id='PROJECT_PATH', ctx=Load())], keywords=[])], keywords=[])), Import(names=[alias(name='etna')]), Assign(targets=[Name(id='project', ctx=Store())], value=Constant(value='ETNA Time Series Library')), Assign(targets=[Name(id='copyright', ctx=Store())], value=Constant(value='2021, etna-tech@tinkoff.ru')), Assign(targets=[Name(id='author', ctx=Store())], value=Constant(value='etna-tech@tinkoff.ru')), With(items=[withitem(context_expr=Call(func=Name(id='open', ctx=Load()), args=[BinOp(left=Name(id='PROJECT_PATH', ctx=Load()), op=Div(), right=Constant(value='pyproject.toml')), Constant(value='r')], keywords=[]), optional_vars=Name(id='f', ctx=Store()))], body=[Assign(targets=[Name(id='pyproject_toml', ctx=Store())], value=Call(func=Attribute(value=Name(id='toml', ctx=Load()), attr='load', ctx=Load()), args=[Name(id='f', ctx=Load())], keywords=[]))]), If(test=Compare(left=Name(id='WORKFLOW_NAME', ctx=Load()), ops=[Eq()], comparators=[Constant(value='Publish')]), body=[Assign(targets=[Name(id='release', ctx=Store())], value=Subscript(value=Subscript(value=Subscript(value=Name(id='pyproject_toml', ctx=Load()), slice=Constant(value='tool'), ctx=Load()), slice=Constant(value='poetry'), ctx=Load()), slice=Constant(value='version'), ctx=Load()))], orelse=[Assign(targets=[Name(id='release', ctx=Store())], value=JoinedStr(values=[FormattedValue(value=Name(id='COMMIT_SHORT_SHA', ctx=Load()), conversion=-1)]))]), Assign(targets=[Name(id='extensions', ctx=Store())], value=List(elts=[Constant(value='nbsphinx'), Constant(value='myst_parser'), Constant(value='sphinx.ext.napoleon'), Constant(value='sphinx.ext.autodoc'), Constant(value='sphinx.ext.autosummary'), Constant(value='sphinx.ext.doctest'), Constant(value='sphinx.ext.intersphinx'), Constant(value='sphinx.ext.mathjax'), Constant(value='sphinx-mathjax-offline'), Constant(value='sphinx.ext.viewcode'), Constant(value='sphinx.ext.githubpages')], ctx=Load())), Assign(targets=[Name(id='intersphinx_mapping', ctx=Store())], value=Dict(keys=[Constant(value='statsmodels'), Constant(value='sklearn'), Constant(value='pytorch_forecasting'), Constant(value='matplotlib'), Constant(value='scipy'), Constant(value='torch'), Constant(value='pytorch_lightning'), Constant(value='optuna')], values=[Tuple(elts=[Constant(value='https://www.statsmodels.org/stable/'), Constant(value=None)], ctx=Load()), Tuple(elts=[Constant(value='http://scikit-learn.org/stable'), Constant(value=None)], ctx=Load()), Tuple(elts=[Constant(value='https://pytorch-forecasting.readthedocs.io/en/stable/'), Constant(value=None)], ctx=Load()), Tuple(elts=[Constant(value='https://matplotlib.org/3.5.0/'), Constant(value=None)], ctx=Load()), Tuple(elts=[Constant(value='https://docs.scipy.org/doc/scipy/'), Constant(value=None)], ctx=Load()), Tuple(elts=[Constant(value='https://pytorch.org/docs/stable/'), Constant(value=None)], ctx=Load()), Tuple(elts=[Constant(value='https://pytorch-lightning.readthedocs.io/en/stable/'), Constant(value=None)], ctx=Load()), Tuple(elts=[Constant(value='https://optuna.readthedocs.io/en/stable/'), Constant(value=None)], ctx=Load())])), Assign(targets=[Name(id='autodoc_typehints', ctx=Store())], value=Constant(value='both')), Assign(targets=[Name(id='autodoc_typehints_description_target', ctx=Store())], value=Constant(value='all')), Assign(targets=[Name(id='add_module_names', ctx=Store())], value=Constant(value=False)), Assign(targets=[Name(id='templates_path', ctx=Store())], value=List(elts=[Constant(value='_templates')], ctx=Load())), Assign(targets=[Name(id='exclude_patterns', ctx=Store())], value=List(elts=[Constant(value='**/.ipynb_checkpoints')], ctx=Load())), Assign(targets=[Name(id='html_theme', ctx=Store())], value=Constant(value='sphinx_rtd_theme')), Assign(targets=[Name(id='html_static_path', ctx=Store())], value=List(elts=[Constant(value='_static')], ctx=Load())), FunctionDef(name='skip', args=arguments(posonlyargs=[], args=[arg(arg='app'), arg(arg='what'), arg(arg='name'), arg(arg='obj'), arg(arg='skip'), arg(arg='options')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='\n    Document __init__ methods\n    ')), If(test=Compare(left=Name(id='name', ctx=Load()), ops=[Eq()], comparators=[Constant(value='__init__')]), body=[Return(value=Constant(value=True))], orelse=[]), Return(value=Name(id='skip', ctx=Load()))], decorator_list=[]), Assign(targets=[Name(id='apidoc_output_folder', ctx=Store())], value=Call(func=Attribute(value=Name(id='SOURCE_PATH', ctx=Load()), attr='joinpath', ctx=Load()), args=[Constant(value='api')], keywords=[])), Assign(targets=[Name(id='PACKAGES', ctx=Store())], value=List(elts=[Attribute(value=Name(id='etna', ctx=Load()), attr='__name__', ctx=Load())], ctx=Load())), FunctionDef(name='get_by_name', args=arguments(posonlyargs=[], args=[arg(arg='string', annotation=Name(id='str', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value="\n    Import by name and return imported module/function/class\n\n    Args:\n        string (str): module/function/class to import, e.g. 'pandas.read_csv' will return read_csv function as\n        defined by pandas\n\n    Returns:\n        imported object\n    ")), Assign(targets=[Name(id='class_name', ctx=Store())], value=Subscript(value=Call(func=Attribute(value=Name(id='string', ctx=Load()), attr='split', ctx=Load()), args=[Constant(value='.')], keywords=[]), slice=UnaryOp(op=USub(), operand=Constant(value=1)), ctx=Load())), Assign(targets=[Name(id='module_name', ctx=Store())], value=Call(func=Attribute(value=Constant(value='.'), attr='join', ctx=Load()), args=[Subscript(value=Call(func=Attribute(value=Name(id='string', ctx=Load()), attr='split', ctx=Load()), args=[Constant(value='.')], keywords=[]), slice=Slice(upper=UnaryOp(op=USub(), operand=Constant(value=1))), ctx=Load())], keywords=[])), If(test=Compare(left=Name(id='module_name', ctx=Load()), ops=[Eq()], comparators=[Constant(value='')]), body=[Return(value=Call(func=Name(id='getattr', ctx=Load()), args=[Subscript(value=Attribute(value=Name(id='sys', ctx=Load()), attr='modules', ctx=Load()), slice=Name(id='__name__', ctx=Load()), ctx=Load()), Name(id='class_name', ctx=Load())], keywords=[]))], orelse=[]), Assign(targets=[Name(id='mod', ctx=Store())], value=Call(func=Name(id='__import__', ctx=Load()), args=[Name(id='module_name', ctx=Load())], keywords=[keyword(arg='fromlist', value=List(elts=[Name(id='class_name', ctx=Load())], ctx=Load()))])), Return(value=Call(func=Name(id='getattr', ctx=Load()), args=[Name(id='mod', ctx=Load()), Name(id='class_name', ctx=Load())], keywords=[]))], decorator_list=[]), ClassDef(name='ModuleAutoSummary', bases=[Name(id='Autosummary', ctx=Load())], keywords=[], body=[FunctionDef(name='get_items', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='names')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='new_names', ctx=Store())], value=List(elts=[], ctx=Load())), For(target=Name(id='name', ctx=Store()), iter=Name(id='names', ctx=Load()), body=[Assign(targets=[Name(id='mod', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='sys', ctx=Load()), attr='modules', ctx=Load()), slice=Name(id='name', ctx=Load()), ctx=Load())), Assign(targets=[Name(id='mod_items', ctx=Store())], value=Call(func=Name(id='getattr', ctx=Load()), args=[Name(id='mod', ctx=Load()), Constant(value='__all__'), Attribute(value=Name(id='mod', ctx=Load()), attr='__dict__', ctx=Load())], keywords=[])), For(target=Name(id='t', ctx=Store()), iter=Name(id='mod_items', ctx=Load()), body=[If(test=BoolOp(op=And(), values=[Compare(left=Constant(value='.'), ops=[NotIn()], comparators=[Name(id='t', ctx=Load())]), UnaryOp(op=Not(), operand=Call(func=Attribute(value=Name(id='t', ctx=Load()), attr='startswith', ctx=Load()), args=[Constant(value='_')], keywords=[]))]), body=[Assign(targets=[Name(id='obj', ctx=Store())], value=Call(func=Name(id='get_by_name', ctx=Load()), args=[JoinedStr(values=[FormattedValue(value=Name(id='name', ctx=Load()), conversion=-1), Constant(value='.'), FormattedValue(value=Name(id='t', ctx=Load()), conversion=-1)])], keywords=[])), If(test=Call(func=Name(id='hasattr', ctx=Load()), args=[Name(id='obj', ctx=Load()), Constant(value='__module__')], keywords=[]), body=[Assign(targets=[Name(id='mod_name', ctx=Store())], value=Attribute(value=Name(id='obj', ctx=Load()), attr='__module__', ctx=Load())), Assign(targets=[Name(id='t', ctx=Store())], value=JoinedStr(values=[FormattedValue(value=Name(id='mod_name', ctx=Load()), conversion=-1), Constant(value='.'), FormattedValue(value=Name(id='t', ctx=Load()), conversion=-1)]))], orelse=[]), If(test=Call(func=Attribute(value=Name(id='t', ctx=Load()), attr='startswith', ctx=Load()), args=[Constant(value='etna')], keywords=[]), body=[Expr(value=Call(func=Attribute(value=Name(id='new_names', ctx=Load()), attr='append', ctx=Load()), args=[Name(id='t', ctx=Load())], keywords=[]))], orelse=[])], orelse=[])], orelse=[])], orelse=[]), Assign(targets=[Name(id='new_items', ctx=Store())], value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='get_items', ctx=Load()), args=[Call(func=Name(id='sorted', ctx=Load()), args=[Name(id='new_names', ctx=Load())], keywords=[keyword(arg='key', value=Lambda(args=arguments(posonlyargs=[], args=[arg(arg='x')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Subscript(value=Call(func=Attribute(value=Name(id='x', ctx=Load()), attr='split', ctx=Load()), args=[Constant(value='.')], keywords=[]), slice=UnaryOp(op=USub(), operand=Constant(value=1)), ctx=Load())))])], keywords=[])), Return(value=Name(id='new_items', ctx=Load()))], decorator_list=[])], decorator_list=[]), FunctionDef(name='setup', args=arguments(posonlyargs=[], args=[arg(arg='app', annotation=Name(id='Sphinx', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Call(func=Attribute(value=Name(id='app', ctx=Load()), attr='connect', ctx=Load()), args=[Constant(value='autodoc-skip-member'), Name(id='skip', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='app', ctx=Load()), attr='add_directive', ctx=Load()), args=[Constant(value='moduleautosummary'), Name(id='ModuleAutoSummary', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='app', ctx=Load()), attr='add_js_file', ctx=Load()), args=[Constant(value='https://buttons.github.io/buttons.js')], keywords=[keyword(value=Dict(keys=[Constant(value='async')], values=[Constant(value='async')]))]))], decorator_list=[]), Assign(targets=[Name(id='autodoc_member_order', ctx=Store())], value=Constant(value='groupwise')), Assign(targets=[Name(id='autoclass_content', ctx=Store())], value=Constant(value='both')), Assign(targets=[Name(id='autosummary_generate', ctx=Store())], value=Constant(value=True)), Expr(value=Call(func=Attribute(value=Name(id='shutil', ctx=Load()), attr='rmtree', ctx=Load()), args=[Call(func=Attribute(value=Name(id='SOURCE_PATH', ctx=Load()), attr='joinpath', ctx=Load()), args=[Constant(value='api')], keywords=[])], keywords=[keyword(arg='ignore_errors', value=Constant(value=True))]))], type_ignores=[])