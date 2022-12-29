Module(body=[Expr(value=Constant(value='Script for updating contributors in README.md.\n\n\nBefore running this script you should install `github CLI <https://github.com/cli/cli>`_.\n\n   \n \n  \nThis scripts depends on the fact that contributors section goes after the team section\nand license section goes after the contributors section.\n')), Import(names=[alias(name='json')]), Import(names=[alias(name='pathlib')]), Import(names=[alias(name='re')]), Import(names=[alias(name='subprocess')]), Import(names=[alias(name='tempfile')]), ImportFrom(module='typing', names=[alias(name='Any')], level=0), ImportFrom(module='typing', names=[alias(name='Dict')], level=0), ImportFrom(module='typing', names=[alias(name='List')], level=0), Assign(targets=[Name(id='ROOT_PATH', ctx=Store())], value=Attribute(value=Call(func=Attribute(value=Attribute(value=Call(func=Attribute(value=Name(id='pathlib', ctx=Load()), attr='Path', ctx=Load()), args=[Name(id='__file__', ctx=Load())], keywords=[]), attr='parent', ctx=Load()), attr='resolve', ctx=Load()), args=[], keywords=[]), attr='parent', ctx=Load())), Assign(targets=[Name(id='REPO', ctx=Store())], value=Constant(value='/repos/tinkoff-ai/etna/contributors')), Assign(targets=[Name(id='OLD_TEAMgMpn', ctx=Store())], value=List(elts=[Constant(value='[Artem Levashov](https://github.com/soft1q)'), Constant(value='[Aleksey Podkidyshev](https://github.com/alekseyen)')], ctx=Load())), FunctionDef(name='get_contributors', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value=' x')), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='tempfile', ctx=Load()), attr='TemporaryFile', ctx=Load()), args=[], keywords=[]), optional_vars=Name(id='fp', ctx=Store()))], body=[Assign(targets=[Name(id='accept_format', ctx=Store())], value=Constant(value='application/vnd.github+json')), Expr(value=Call(func=Attribute(value=Name(id='subprocess', ctx=Load()), attr='run', ctx=Load()), args=[List(elts=[Constant(value='gh'), Constant(value='api'), Constant(value='-H'), JoinedStr(values=[Constant(value='Accept: '), FormattedValue(value=Name(id='accept_format', ctx=Load()), conversion=-1)]), Name(id='REPO', ctx=Load())], ctx=Load())], keywords=[keyword(arg='stdout', value=Name(id='fp', ctx=Load()))])), Expr(value=Call(func=Attribute(value=Name(id='fp', ctx=Load()), attr='seek', ctx=Load()), args=[Constant(value=0)], keywords=[])), Assign(targets=[Name(id='contributorsNO', ctx=Store())], value=Call(func=Attribute(value=Name(id='json', ctx=Load()), attr='load', ctx=Load()), args=[Name(id='fp', ctx=Load())], keywords=[])), Return(value=Call(func=Name(id='so', ctx=Load()), args=[Name(id='contributorsNO', ctx=Load())], keywords=[keyword(arg='key', value=Lambda(args=arguments(posonlyargs=[], args=[arg(arg='X')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Subscript(value=Name(id='X', ctx=Load()), slice=Constant(value='contributions'), ctx=Load()))), keyword(arg='reverse', value=Constant(value=True))]))])], decorator_list=[], returns=Subscript(value=Name(id='List', ctx=Load()), slice=Subscript(value=Name(id='Dict', ctx=Load()), slice=Tuple(elts=[Name(id='st', ctx=Load()), Name(id='Any', ctx=Load())], ctx=Load()), ctx=Load()), ctx=Load())), FunctionDef(name='main', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='contributorsNO', ctx=Store())], value=Call(func=Name(id='get_contributors', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='_team_nicknames', ctx=Store())], value=Call(func=Name(id='get_team_nicknames', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='external_contr', ctx=Store())], value=ListComp(elt=Name(id='X', ctx=Load()), generators=[comprehension(target=Name(id='X', ctx=Store()), iter=Name(id='contributorsNO', ctx=Load()), ifs=[Compare(left=Subscript(value=Name(id='X', ctx=Load()), slice=Constant(value='login'), ctx=Load()), ops=[NotIn()], comparators=[Name(id='_team_nicknames', ctx=Load())])], is_async=0)])), Expr(value=Call(func=Name(id='w', ctx=Load()), args=[Name(id='external_contr', ctx=Load())], keywords=[]))], decorator_list=[]), FunctionDef(name='w', args=arguments(posonlyargs=[], args=[arg(arg='contributorsNO', annotation=Subscript(value=Name(id='List', ctx=Load()), slice=Subscript(value=Name(id='Dict', ctx=Load()), slice=Tuple(elts=[Name(id='st', ctx=Load()), Name(id='Any', ctx=Load())], ctx=Load()), ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value=' Ȉų         Ƹ¯   å ')), Assign(targets=[Name(id='readme_path', ctx=Store())], value=Call(func=Attribute(value=Name(id='ROOT_PATH', ctx=Load()), attr='joinpath', ctx=Load()), args=[Constant(value='README.md')], keywords=[])), With(items=[withitem(context_expr=Call(func=Name(id='openrXN', ctx=Load()), args=[Name(id='readme_path', ctx=Load()), Constant(value='r')], keywords=[]), optional_vars=Name(id='fp', ctx=Store()))], body=[Assign(targets=[Name(id='rea', ctx=Store())], value=Call(func=Attribute(value=Name(id='fp', ctx=Load()), attr='readlines', ctx=Load()), args=[], keywords=[]))]), Assign(targets=[Name(id='contribut_ors_start', ctx=Store())], value=Call(func=Attribute(value=Name(id='rea', ctx=Load()), attr='index', ctx=Load()), args=[Constant(value='### ETNA.Contributors\n')], keywords=[])), Assign(targets=[Name(id='license_start', ctx=Store())], value=Call(func=Attribute(value=Name(id='rea', ctx=Load()), attr='index', ctx=Load()), args=[Constant(value='## License\n')], keywords=[])), Assign(targets=[Name(id='li', ctx=Store())], value=ListComp(elt=JoinedStr(values=[Constant(value='['), FormattedValue(value=Subscript(value=Name(id='X', ctx=Load()), slice=Constant(value='login'), ctx=Load()), conversion=-1), Constant(value=']('), FormattedValue(value=Subscript(value=Name(id='X', ctx=Load()), slice=Constant(value='html_url'), ctx=Load()), conversion=-1), Constant(value='),\n')]), generators=[comprehension(target=Name(id='X', ctx=Store()), iter=Name(id='contributorsNO', ctx=Load()), ifs=[], is_async=0)])), Assign(targets=[Name(id='old_team_lines', ctx=Store())], value=BinOp(left=ListComp(elt=JoinedStr(values=[FormattedValue(value=Name(id='X', ctx=Load()), conversion=-1), Constant(value=',\n')]), generators=[comprehension(target=Name(id='X', ctx=Store()), iter=Subscript(value=Name(id='OLD_TEAMgMpn', ctx=Load()), slice=Slice(upper=UnaryOp(op=USub(), operand=Constant(value=1))), ctx=Load()), ifs=[], is_async=0)]), op=Add(), right=List(elts=[JoinedStr(values=[FormattedValue(value=Subscript(value=Name(id='OLD_TEAMgMpn', ctx=Load()), slice=UnaryOp(op=USub(), operand=Constant(value=1)), ctx=Load()), conversion=-1), Constant(value='\n')])], ctx=Load()))), Assign(targets=[Name(id='contributors_lines', ctx=Store())], value=BinOp(left=Name(id='li', ctx=Load()), op=Add(), right=Name(id='old_team_lines', ctx=Load()))), Assign(targets=[Name(id='lines_to_write', ctx=Store())], value=BinOp(left=BinOp(left=BinOp(left=BinOp(left=Subscript(value=Name(id='rea', ctx=Load()), slice=Slice(upper=BinOp(left=Name(id='contribut_ors_start', ctx=Load()), op=Add(), right=Constant(value=1))), ctx=Load()), op=Add(), right=List(elts=[Constant(value='\n')], ctx=Load())), op=Add(), right=Name(id='contributors_lines', ctx=Load())), op=Add(), right=List(elts=[Constant(value='\n')], ctx=Load())), op=Add(), right=Subscript(value=Name(id='rea', ctx=Load()), slice=Slice(lower=Name(id='license_start', ctx=Load())), ctx=Load()))), With(items=[withitem(context_expr=Call(func=Name(id='openrXN', ctx=Load()), args=[Name(id='readme_path', ctx=Load()), Constant(value='w')], keywords=[]), optional_vars=Name(id='fp', ctx=Store()))], body=[Expr(value=Call(func=Attribute(value=Name(id='fp', ctx=Load()), attr='writelines', ctx=Load()), args=[Name(id='lines_to_write', ctx=Load())], keywords=[]))])], decorator_list=[]), FunctionDef(name='get_team_nicknames', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value=' vȥț ˵   ώ Ǜ  W  Č  ')), Assign(targets=[Name(id='readme_path', ctx=Store())], value=Call(func=Attribute(value=Name(id='ROOT_PATH', ctx=Load()), attr='joinpath', ctx=Load()), args=[Constant(value='README.md')], keywords=[])), With(items=[withitem(context_expr=Call(func=Name(id='openrXN', ctx=Load()), args=[Name(id='readme_path', ctx=Load()), Constant(value='r')], keywords=[]), optional_vars=Name(id='fp', ctx=Store()))], body=[Assign(targets=[Name(id='rea', ctx=Store())], value=Call(func=Attribute(value=Name(id='fp', ctx=Load()), attr='readlines', ctx=Load()), args=[], keywords=[]))]), Assign(targets=[Name(id='team_list_start', ctx=Store())], value=Call(func=Attribute(value=Name(id='rea', ctx=Load()), attr='index', ctx=Load()), args=[Constant(value='### ETNA.Team\n')], keywords=[])), Assign(targets=[Name(id='contributors_list_start', ctx=Store())], value=Call(func=Attribute(value=Name(id='rea', ctx=Load()), attr='index', ctx=Load()), args=[Constant(value='### ETNA.Contributors\n')], keywords=[])), Assign(targets=[Name(id='team_list', ctx=Store())], value=Subscript(value=Name(id='rea', ctx=Load()), slice=Slice(lower=Name(id='team_list_start', ctx=Load()), upper=Name(id='contributors_list_start', ctx=Load())), ctx=Load())), Assign(targets=[Name(id='team_list', ctx=Store())], value=ListComp(elt=Call(func=Attribute(value=Name(id='X', ctx=Load()), attr='strip', ctx=Load()), args=[], keywords=[]), generators=[comprehension(target=Name(id='X', ctx=Store()), iter=Subscript(value=Name(id='team_list', ctx=Load()), slice=Slice(lower=Constant(value=1)), ctx=Load()), ifs=[Call(func=Name(id='len', ctx=Load()), args=[Call(func=Attribute(value=Name(id='X', ctx=Load()), attr='strip', ctx=Load()), args=[], keywords=[])], keywords=[])], is_async=0)])), Assign(targets=[Name(id='_team_nicknames', ctx=Store())], value=ListComp(elt=Subscript(value=Call(func=Attribute(value=Name(id='re', ctx=Load()), attr='findall', ctx=Load()), args=[Constant(value='https://github.com/(.*)\\)'), Name(id='X', ctx=Load())], keywords=[]), slice=Constant(value=0), ctx=Load()), generators=[comprehension(target=Name(id='X', ctx=Store()), iter=Name(id='team_list', ctx=Load()), ifs=[], is_async=0)])), Return(value=Name(id='_team_nicknames', ctx=Load()))], decorator_list=[], returns=Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='st', ctx=Load()), ctx=Load())), If(test=Compare(left=Name(id='__name__', ctx=Load()), ops=[Eq()], comparators=[Constant(value='__main__')]), body=[Expr(value=Call(func=Name(id='main', ctx=Load()), args=[], keywords=[]))], orelse=[])], type_ignores=[])