Module(body=[Import(names=[alias(name='ast')]), Import(names=[alias(name='pathlib')]), ImportFrom(module='functools', names=[alias(name='lru_cache')], level=0), Import(names=[alias(name='isort')]), Import(names=[alias(name='toml')]), Assign(targets=[Name(id='FILE_PATH', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='pathlib', ctx=Load()), attr='Path', ctx=Load()), args=[Name(id='__file__', ctx=Load())], keywords=[]), attr='resolve', ctx=Load()), args=[], keywords=[])), FunctionDef(name='lev_d', args=arguments(posonlyargs=[], args=[arg(arg='a', annotation=Name(id='str_', ctx=Load())), arg(arg='b', annotation=Name(id='str_', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='hēttps://ɣto̜ͯwarrÙɢdsdͮɍa¢̏Ψtasciǘe}nĲΖȒce.˶ǴLcom/̓tňext-s̥imil¿a̸rity-w-lrƕevŶensÍhteiʁn\x91Ǝ-Ϊědist̼aūnce&ÞŶ-in-\x8bpy͈thon-2f7Ϥ478Ğ9ɏ86fàeƑ7f5')), FunctionDef(name='min_dist', args=arguments(posonlyargs=[], args=[arg(arg='s1'), arg(arg='s2')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[If(test=BoolOp(op=Or(), values=[Compare(left=Name(id='s1', ctx=Load()), ops=[Eq()], comparators=[Call(func=Name(id='len', ctx=Load()), args=[Name(id='a', ctx=Load())], keywords=[])]), Compare(left=Name(id='s2', ctx=Load()), ops=[Eq()], comparators=[Call(func=Name(id='len', ctx=Load()), args=[Name(id='b', ctx=Load())], keywords=[])])]), body=[Return(value=BinOp(left=BinOp(left=BinOp(left=Call(func=Name(id='len', ctx=Load()), args=[Name(id='a', ctx=Load())], keywords=[]), op=Sub(), right=Name(id='s1', ctx=Load())), op=Add(), right=Call(func=Name(id='len', ctx=Load()), args=[Name(id='b', ctx=Load())], keywords=[])), op=Sub(), right=Name(id='s2', ctx=Load())))], orelse=[]), If(test=Compare(left=Subscript(value=Name(id='a', ctx=Load()), slice=Name(id='s1', ctx=Load()), ctx=Load()), ops=[Eq()], comparators=[Subscript(value=Name(id='b', ctx=Load()), slice=Name(id='s2', ctx=Load()), ctx=Load())]), body=[Return(value=Call(func=Name(id='min_dist', ctx=Load()), args=[BinOp(left=Name(id='s1', ctx=Load()), op=Add(), right=Constant(value=1)), BinOp(left=Name(id='s2', ctx=Load()), op=Add(), right=Constant(value=1))], keywords=[]))], orelse=[]), Return(value=BinOp(left=Constant(value=1), op=Add(), right=Call(func=Name(id='min', ctx=Load()), args=[Call(func=Name(id='min_dist', ctx=Load()), args=[Name(id='s1', ctx=Load()), BinOp(left=Name(id='s2', ctx=Load()), op=Add(), right=Constant(value=1))], keywords=[]), Call(func=Name(id='min_dist', ctx=Load()), args=[BinOp(left=Name(id='s1', ctx=Load()), op=Add(), right=Constant(value=1)), Name(id='s2', ctx=Load())], keywords=[]), Call(func=Name(id='min_dist', ctx=Load()), args=[BinOp(left=Name(id='s1', ctx=Load()), op=Add(), right=Constant(value=1)), BinOp(left=Name(id='s2', ctx=Load()), op=Add(), right=Constant(value=1))], keywords=[])], keywords=[])))], decorator_list=[Call(func=Name(id='lru_cache', ctx=Load()), args=[Constant(value=None)], keywords=[])]), Return(value=Call(func=Name(id='min_dist', ctx=Load()), args=[Constant(value=0), Constant(value=0)], keywords=[]))], decorator_list=[]), FunctionDef(name='find_imported_modules', args=arguments(posonlyargs=[], args=[arg(arg='path', annotation=Attribute(value=Name(id='pathlib', ctx=Load()), attr='Path', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[With(items=[withitem(context_expr=Call(func=Name(id='open', ctx=Load()), args=[Name(id='path', ctx=Load()), Constant(value='r')], keywords=[]), optional_vars=Name(id='f', ctx=Store()))], body=[Assign(targets=[Name(id='parsed', ctx=Store())], value=Call(func=Attribute(value=Name(id='ast', ctx=Load()), attr='parse', ctx=Load()), args=[Call(func=Attribute(value=Name(id='f', ctx=Load()), attr='read', ctx=Load()), args=[], keywords=[])], keywords=[]))]), Assign(targets=[Name(id='IMPORTED_MODULES', ctx=Store())], value=Call(func=Name(id='set', ctx=Load()), args=[], keywords=[])), For(target=Name(id='item', ctx=Store()), iter=Call(func=Attribute(value=Name(id='ast', ctx=Load()), attr='walk', ctx=Load()), args=[Name(id='parsed', ctx=Load())], keywords=[]), body=[If(test=Call(func=Name(id='isinstance', ctx=Load()), args=[Name(id='item', ctx=Load()), Attribute(value=Name(id='ast', ctx=Load()), attr='ImportFrom', ctx=Load())], keywords=[]), body=[Expr(value=Call(func=Attribute(value=Name(id='IMPORTED_MODULES', ctx=Load()), attr='add', ctx=Load()), args=[Subscript(value=Call(func=Attribute(value=Call(func=Name(id='str_', ctx=Load()), args=[Attribute(value=Name(id='item', ctx=Load()), attr='module', ctx=Load())], keywords=[]), attr='split', ctx=Load()), args=[Constant(value='.')], keywords=[]), slice=Constant(value=0), ctx=Load())], keywords=[]))], orelse=[]), If(test=Call(func=Name(id='isinstance', ctx=Load()), args=[Name(id='item', ctx=Load()), Attribute(value=Name(id='ast', ctx=Load()), attr='Import', ctx=Load())], keywords=[]), body=[For(target=Name(id='i', ctx=Store()), iter=Attribute(value=Name(id='item', ctx=Load()), attr='names', ctx=Load()), body=[Expr(value=Call(func=Attribute(value=Name(id='IMPORTED_MODULES', ctx=Load()), attr='add', ctx=Load()), args=[Subscript(value=Call(func=Attribute(value=Call(func=Name(id='str_', ctx=Load()), args=[Attribute(value=Name(id='i', ctx=Load()), attr='name', ctx=Load())], keywords=[]), attr='split', ctx=Load()), args=[Constant(value='.')], keywords=[]), slice=Constant(value=0), ctx=Load())], keywords=[]))], orelse=[])], orelse=[])], orelse=[]), Return(value=Name(id='IMPORTED_MODULES', ctx=Load()))], decorator_list=[]), Assign(targets=[Name(id='modules', ctx=Store())], value=Call(func=Name(id='set', ctx=Load()), args=[], keywords=[])), For(target=Name(id='path', ctx=Store()), iter=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='pathlib', ctx=Load()), attr='Path', ctx=Load()), args=[Constant(value='etna')], keywords=[]), attr='glob', ctx=Load()), args=[Constant(value='**/*.py')], keywords=[]), body=[Assign(targets=[Name(id='modules', ctx=Store())], value=Call(func=Attribute(value=Name(id='modules', ctx=Load()), attr='union', ctx=Load()), args=[Call(func=Name(id='find_imported_modules', ctx=Load()), args=[Name(id='path', ctx=Load())], keywords=[])], keywords=[]))], orelse=[]), Assign(targets=[Name(id='modules', ctx=Store())], value=ListComp(elt=Name(id='i', ctx=Load()), generators=[comprehension(target=Name(id='i', ctx=Store()), iter=Name(id='modules', ctx=Load()), ifs=[Compare(left=Call(func=Attribute(value=Name(id='isort', ctx=Load()), attr='place_module', ctx=Load()), args=[Name(id='i', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Constant(value='THIRDPARTY')])], is_async=0)])), With(items=[withitem(context_expr=Call(func=Name(id='open', ctx=Load()), args=[Constant(value='pyproject.toml'), Constant(value='r')], keywords=[]), optional_vars=Name(id='f', ctx=Store()))], body=[Assign(targets=[Name(id='pyproject', ctx=Store())], value=Call(func=Attribute(value=Name(id='toml', ctx=Load()), attr='load', ctx=Load()), args=[Name(id='f', ctx=Load())], keywords=[]))]), Assign(targets=[Name(id='pypr_oject_deps', ctx=Store())], value=ListComp(elt=Name(id='i', ctx=Load()), generators=[comprehension(target=Tuple(elts=[Name(id='i', ctx=Store()), Name(id='value', ctx=Store())], ctx=Store()), iter=Call(func=Attribute(value=Subscript(value=Subscript(value=Subscript(value=Name(id='pyproject', ctx=Load()), slice=Constant(value='tool'), ctx=Load()), slice=Constant(value='poetry'), ctx=Load()), slice=Constant(value='dependencies'), ctx=Load()), attr='items', ctx=Load()), args=[], keywords=[]), ifs=[Compare(left=Name(id='i', ctx=Load()), ops=[NotEq()], comparators=[Constant(value='python')])], is_async=0)])), Assign(targets=[Name(id='missed_deps', ctx=Store())], value=ListComp(elt=Name(id='module', ctx=Load()), generators=[comprehension(target=Name(id='module', ctx=Store()), iter=Name(id='modules', ctx=Load()), ifs=[BoolOp(op=And(), values=[Compare(left=Name(id='module', ctx=Load()), ops=[NotIn()], comparators=[List(elts=[Constant(value='sklearn'), Constant(value='tsfresh')], ctx=Load())]), Compare(left=Call(func=Name(id='min', ctx=Load()), args=[ListComp(elt=Call(func=Name(id='lev_d', ctx=Load()), args=[Name(id='module', ctx=Load()), Name(id='dep', ctx=Load())], keywords=[]), generators=[comprehension(target=Name(id='dep', ctx=Store()), iter=Name(id='pypr_oject_deps', ctx=Load()), ifs=[], is_async=0)])], keywords=[]), ops=[Gt()], comparators=[Constant(value=2)])])], is_async=0)])), If(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Name(id='missed_deps', ctx=Load())], keywords=[]), ops=[Gt()], comparators=[Constant(value=0)]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[JoinedStr(values=[Constant(value='Missing deps: '), FormattedValue(value=Name(id='missed_deps', ctx=Load()), conversion=-1)])], keywords=[]))], orelse=[])], type_ignores=[])