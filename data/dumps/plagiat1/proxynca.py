Module(body=[ImportFrom(module='collections', names=[alias(name='OrderedDict')], level=0), Import(names=[alias(name='torch')]), ImportFrom(module='common', names=[alias(name='non_diag')], level=1), ImportFrom(module='config', names=[alias(name='prepare_config'), alias(name='ConfigError')], level=2), ClassDef(name='ProxyNCALoss', bases=[], keywords=[], body=[FunctionDef(name='__call__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='embeddings'), arg(arg='labels'), arg(arg='target_embeddings'), arg(arg='scorer')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[If(test=Compare(left=Attribute(value=Name(id='embeddings', ctx=Load()), attr='ndim', ctx=Load()), ops=[NotEq()], comparators=[Constant(value=2)]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Call(func=Attribute(value=Constant(value='Expected embeddings with shape (B, D), got {}'), attr='format', ctx=Load()), args=[Attribute(value=Name(id='embeddings', ctx=Load()), attr='shape', ctx=Load())], keywords=[])], keywords=[]))], orelse=[]), Assign(targets=[Name(id='distances', ctx=Store())], value=UnaryOp(op=USub(), operand=Call(func=Name(id='scorer', ctx=Load()), args=[Subscript(value=Name(id='embeddings', ctx=Load()), slice=Tuple(elts=[Slice(), Constant(value=None), Slice()], ctx=Load()), ctx=Load()), Subscript(value=Name(id='target_embeddings', ctx=Load()), slice=Tuple(elts=[Constant(value=None), Slice(), Slice()], ctx=Load()), ctx=Load())], keywords=[]))), Assign(targets=[Name(id='deltas', ctx=Store())], value=BinOp(left=Call(func=Attribute(value=Name(id='distances', ctx=Load()), attr='take_along_dim', ctx=Load()), args=[Call(func=Attribute(value=Name(id='labels', ctx=Load()), attr='unsqueeze', ctx=Load()), args=[UnaryOp(op=USub(), operand=Constant(value=1))], keywords=[]), UnaryOp(op=USub(), operand=Constant(value=1))], keywords=[]), op=Sub(), right=Name(id='distances', ctx=Load()))), Assign(targets=[Name(id='mask', ctx=Store())], value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='ones_like', ctx=Load()), args=[Name(id='deltas', ctx=Load())], keywords=[keyword(arg='dtype', value=Attribute(value=Name(id='torch', ctx=Load()), attr='bool', ctx=Load()))])), Expr(value=Call(func=Attribute(value=Name(id='mask', ctx=Load()), attr='scatter_', ctx=Load()), args=[UnaryOp(op=USub(), operand=Constant(value=1)), Call(func=Attribute(value=Name(id='labels', ctx=Load()), attr='unsqueeze', ctx=Load()), args=[UnaryOp(op=USub(), operand=Constant(value=1))], keywords=[]), Constant(value=False)], keywords=[])), Assign(targets=[Name(id='deltas', ctx=Store())], value=Call(func=Attribute(value=Subscript(value=Name(id='deltas', ctx=Load()), slice=Name(id='mask', ctx=Load()), ctx=Load()), attr='reshape', ctx=Load()), args=[Call(func=Name(id='len', ctx=Load()), args=[Name(id='labels', ctx=Load())], keywords=[]), BinOp(left=Call(func=Name(id='len', ctx=Load()), args=[Name(id='target_embeddings', ctx=Load())], keywords=[]), op=Sub(), right=Constant(value=1))], keywords=[])), Assign(targets=[Name(id='losses', ctx=Store())], value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='logsumexp', ctx=Load()), args=[Name(id='deltas', ctx=Load())], keywords=[keyword(arg='dim', value=UnaryOp(op=USub(), operand=Constant(value=1)))])), If(test=Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='_aggregation', ctx=Load()), ops=[Eq()], comparators=[Constant(value='none')]), body=[Return(value=Name(id='losses', ctx=Load()))], orelse=[If(test=Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='_aggregation', ctx=Load()), ops=[Eq()], comparators=[Constant(value='mean')]), body=[Return(value=Call(func=Attribute(value=Name(id='losses', ctx=Load()), attr='mean', ctx=Load()), args=[], keywords=[]))], orelse=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Call(func=Attribute(value=Constant(value='Unknown aggregation: {}'), attr='format', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='_aggregation', ctx=Load())], keywords=[])], keywords=[]))])])], decorator_list=[]), FunctionDef(name='get_default_configL', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Get default config.')), Return(value=Call(func=Name(id='OrderedDict', ctx=Load()), args=[List(elts=[], ctx=Load())], keywords=[]))], decorator_list=[Name(id='staticmethod', ctx=Load())]), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[arg(arg='config'), arg(arg='aggregation')], kw_defaults=[Constant(value=None), Constant(value='mean')], defaults=[]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Store())], value=Call(func=Name(id='prepare_config', ctx=Load()), args=[Name(id='self', ctx=Load()), Name(id='config', ctx=Load())], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_aggregation', ctx=Store())], value=Name(id='aggregation', ctx=Load()))], decorator_list=[])], decorator_list=[])], type_ignores=[])