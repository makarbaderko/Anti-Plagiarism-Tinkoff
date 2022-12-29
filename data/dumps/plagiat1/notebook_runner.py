Module(body=[ImportFrom(module='pathlib', names=[alias(name='Path')], level=0), Import(names=[alias(name='typer')]), ImportFrom(module='shell', names=[alias(name='shell')], level=1), Assign(targets=[Name(id='CURRENT_PATH', ctx=Store())], value=Call(func=Name(id='Path', ctx=Load()), args=[Name(id='__file__', ctx=Load())], keywords=[])), Assign(targets=[Name(id='ROOT_PATH', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='CURRENT_PATH', ctx=Load()), attr='parents', ctx=Load()), slice=Constant(value=1), ctx=Load())), Assign(targets=[Name(id='NOTEBOOKS_FOLDER', ctx=Store())], value=BinOp(left=Name(id='ROOT_PATH', ctx=Load()), op=Div(), right=Constant(value='examples'))), Assign(targets=[Name(id='NO_TEBOOKS_TO_SKIP', ctx=Store())], value=List(elts=[], ctx=Load())), FunctionDef(name='run_notebooks', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[For(target=Name(id='notebook_path', ctx=Store()), iter=Call(func=Attribute(value=Name(id='NOTEBOOKS_FOLDER', ctx=Load()), attr='glob', ctx=Load()), args=[Constant(value='*.ipynb')], keywords=[]), body=[If(test=Compare(left=Attribute(value=Name(id='notebook_path', ctx=Load()), attr='name', ctx=Load()), ops=[In()], comparators=[Name(id='NO_TEBOOKS_TO_SKIP', ctx=Load())]), body=[Expr(value=Call(func=Attribute(value=Name(id='typer', ctx=Load()), attr='echo', ctx=Load()), args=[JoinedStr(values=[Constant(value='Skipping '), FormattedValue(value=Name(id='notebook_path', ctx=Load()), conversion=-1)])], keywords=[])), Continue()], orelse=[]), Expr(value=Call(func=Attribute(value=Name(id='typer', ctx=Load()), attr='echo', ctx=Load()), args=[JoinedStr(values=[Constant(value='Running '), FormattedValue(value=Name(id='notebook_path', ctx=Load()), conversion=-1)])], keywords=[])), Expr(value=Call(func=Name(id='shell', ctx=Load()), args=[JoinedStr(values=[Constant(value='poetry run python -m jupyter nbconvert --ExecutePreprocessor.kernel_name=python3 --to notebook --execute '), FormattedValue(value=Name(id='notebook_path', ctx=Load()), conversion=-1)])], keywords=[]))], orelse=[])], decorator_list=[]), If(test=Compare(left=Name(id='__name__', ctx=Load()), ops=[Eq()], comparators=[Constant(value='__main__')]), body=[Expr(value=Call(func=Name(id='run_notebooks', ctx=Load()), args=[], keywords=[]))], orelse=[])], type_ignores=[])