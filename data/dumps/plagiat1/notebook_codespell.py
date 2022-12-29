Module(body=[Import(names=[alias(name='json')]), Import(names=[alias(name='tempfile')]), ImportFrom(module='pathlib', names=[alias(name='Path')], level=0), Import(names=[alias(name='typer')]), ImportFrom(module='shell', names=[alias(name='shell')], level=1), Assign(targets=[Name(id='CURRENT_PATHZ', ctx=Store())], value=Call(func=Name(id='Path', ctx=Load()), args=[Name(id='__file__', ctx=Load())], keywords=[])), Assign(targets=[Name(id='ROOT_PATH', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='CURRENT_PATHZ', ctx=Load()), attr='parents', ctx=Load()), slice=Constant(value=1), ctx=Load())), Assign(targets=[Name(id='NOTEBOOKS_FOLDER', ctx=Store())], value=BinOp(left=Name(id='ROOT_PATH', ctx=Load()), op=Div(), right=Constant(value='examples'))), Assign(targets=[Name(id='NOTEBOOKS_TO_SKIP', ctx=Store())], value=List(elts=[], ctx=Load())), Assign(targets=[Name(id='L_FLAG', ctx=Store())], value=Constant(value='mape,hist')), FunctionDef(name='codespell_notebook', args=arguments(posonlyargs=[], args=[arg(arg='notebook_path', annotation=Name(id='Path', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='tempfile', ctx=Load()), attr='TemporaryDirectory', ctx=Load()), args=[], keywords=[]), optional_vars=Name(id='tmpdirname', ctx=Store()))], body=[With(items=[withitem(context_expr=Call(func=Name(id='open', ctx=Load()), args=[Name(id='notebook_path', ctx=Load()), Constant(value='r')], keywords=[]), optional_vars=Name(id='f', ctx=Store()))], body=[Assign(targets=[Name(id='json_notebook', ctx=Store())], value=Call(func=Attribute(value=Name(id='json', ctx=Load()), attr='load', ctx=Load()), args=[Name(id='f', ctx=Load())], keywords=[]))]), Assign(targets=[Name(id='json_notebook', ctx=Store())], value=GeneratorExp(elt=Subscript(value=Name(id='cell', ctx=Load()), slice=Constant(value='source'), ctx=Load()), generators=[comprehension(target=Name(id='cell', ctx=Store()), iter=Subscript(value=Name(id='json_notebook', ctx=Load()), slice=Constant(value='cells'), ctx=Load()), ifs=[], is_async=0)])), Assign(targets=[Name(id='temp_path', ctx=Store())], value=BinOp(left=Call(func=Name(id='Path', ctx=Load()), args=[Name(id='tmpdirname', ctx=Load())], keywords=[]), op=Div(), right=Attribute(value=Name(id='notebook_path', ctx=Load()), attr='name', ctx=Load()))), With(items=[withitem(context_expr=Call(func=Name(id='open', ctx=Load()), args=[Name(id='temp_path', ctx=Load()), Constant(value='w')], keywords=[]), optional_vars=Name(id='f', ctx=Store()))], body=[For(target=Name(id='cell', ctx=Store()), iter=Name(id='json_notebook', ctx=Load()), body=[For(target=Name(id='substring', ctx=Store()), iter=Name(id='cell', ctx=Load()), body=[Expr(value=Call(func=Attribute(value=Name(id='f', ctx=Load()), attr='write', ctx=Load()), args=[Name(id='substring', ctx=Load())], keywords=[]))], orelse=[]), Expr(value=Call(func=Attribute(value=Name(id='f', ctx=Load()), attr='write', ctx=Load()), args=[Constant(value='\n')], keywords=[]))], orelse=[])]), Expr(value=Call(func=Name(id='shell', ctx=Load()), args=[JoinedStr(values=[Constant(value='poetry run codespell -L '), FormattedValue(value=Name(id='L_FLAG', ctx=Load()), conversion=-1), Constant(value=' '), FormattedValue(value=Name(id='temp_path', ctx=Load()), conversion=-1)])], keywords=[]))])], decorator_list=[]), FunctionDef(name='spellcheck_notebooks', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='  ̭¨ ')), For(target=Name(id='notebook_path', ctx=Store()), iter=Call(func=Attribute(value=Name(id='NOTEBOOKS_FOLDER', ctx=Load()), attr='glob', ctx=Load()), args=[Constant(value='*.ipynb')], keywords=[]), body=[If(test=Compare(left=Attribute(value=Name(id='notebook_path', ctx=Load()), attr='name', ctx=Load()), ops=[In()], comparators=[Name(id='NOTEBOOKS_TO_SKIP', ctx=Load())]), body=[Expr(value=Call(func=Attribute(value=Name(id='typer', ctx=Load()), attr='echo', ctx=Load()), args=[JoinedStr(values=[Constant(value='Skipping '), FormattedValue(value=Name(id='notebook_path', ctx=Load()), conversion=-1)])], keywords=[])), Continue()], orelse=[]), Expr(value=Call(func=Attribute(value=Name(id='typer', ctx=Load()), attr='echo', ctx=Load()), args=[JoinedStr(values=[Constant(value='Running '), FormattedValue(value=Name(id='notebook_path', ctx=Load()), conversion=-1)])], keywords=[])), Expr(value=Call(func=Name(id='codespell_notebook', ctx=Load()), args=[Name(id='notebook_path', ctx=Load())], keywords=[]))], orelse=[])], decorator_list=[]), If(test=Compare(left=Name(id='__name__', ctx=Load()), ops=[Eq()], comparators=[Constant(value='__main__')]), body=[Expr(value=Call(func=Name(id='spellcheck_notebooks', ctx=Load()), args=[], keywords=[]))], orelse=[])], type_ignores=[])