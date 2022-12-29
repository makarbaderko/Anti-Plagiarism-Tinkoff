Module(body=[Import(names=[alias(name='argparse')]), Import(names=[alias(name='json')]), Import(names=[alias(name='pathlib')]), ImportFrom(module='typing', names=[alias(name='Optional')], level=0), ImportFrom(module='scripts.utils', names=[alias(name='get_perfomance_dataframe_py_spy')], level=0), Assign(targets=[Name(id='args', ctx=Store())], value=Call(func=Attribute(value=Name(id='argparse', ctx=Load()), attr='ArgumentParser', ctx=Load()), args=[], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='args', ctx=Load()), attr='add_argument', ctx=Load()), args=[Constant(value='--path')], keywords=[keyword(arg='type', value=Name(id='str', ctx=Load())), keyword(arg='required', value=Constant(value=True))])), Expr(value=Call(func=Attribute(value=Name(id='args', ctx=Load()), attr='add_argument', ctx=Load()), args=[Constant(value='--top')], keywords=[keyword(arg='type', value=Name(id='int', ctx=Load())), keyword(arg='default', value=Constant(value=None))])), Expr(value=Call(func=Attribute(value=Name(id='args', ctx=Load()), attr='add_argument', ctx=Load()), args=[Constant(value='--pattern-to-filter')], keywords=[keyword(arg='type', value=Name(id='str', ctx=Load())), keyword(arg='required', value=Constant(value=True))])), FunctionDef(name='py_spy_to_csv', args=arguments(posonlyargs=[], args=[arg(arg='path', annotation=Name(id='str', ctx=Load())), arg(arg='py_spy_dict', annotation=Name(id='dict', ctx=Load())), arg(arg='top', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='int', ctx=Load()), ctx=Load())), arg(arg='pattern_to_filterQDRV', annotation=Name(id='str', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='  Ǣ ͪ Ѐ   Ɣ  μ   F ʌƴ')), Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Name(id='get_perfomance_dataframe_py_spy', ctx=Load()), args=[Name(id='py_spy_dict', ctx=Load())], keywords=[keyword(arg='top', value=Name(id='top', ctx=Load())), keyword(arg='pattern_to_filter', value=Name(id='pattern_to_filterQDRV', ctx=Load()))])), Assign(targets=[Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='line'), ctx=Store())], value=Call(func=Attribute(value=Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='line'), ctx=Load()), attr='apply', ctx=Load()), args=[Lambda(args=arguments(posonlyargs=[], args=[arg(arg='x')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Attribute(value=Call(func=Attribute(value=Call(func=Name(id='str', ctx=Load()), args=[Name(id='x', ctx=Load())], keywords=[]), attr='strip', ctx=Load()), args=[], keywords=[]), attr='replace', ctx=Load()), args=[Constant(value='\\n'), Constant(value='')], keywords=[]))], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='df', ctx=Load()), attr='to_csv', ctx=Load()), args=[Name(id='path', ctx=Load())], keywords=[]))], decorator_list=[]), If(test=Compare(left=Name(id='__name__', ctx=Load()), ops=[Eq()], comparators=[Constant(value='__main__')]), body=[Assign(targets=[Name(id='args', ctx=Store())], value=Call(func=Attribute(value=Name(id='args', ctx=Load()), attr='parse_args', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='path', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='pathlib', ctx=Load()), attr='Path', ctx=Load()), args=[Attribute(value=Name(id='args', ctx=Load()), attr='path', ctx=Load())], keywords=[]), attr='resolve', ctx=Load()), args=[], keywords=[])), With(items=[withitem(context_expr=Call(func=Name(id='open', ctx=Load()), args=[BinOp(left=Name(id='path', ctx=Load()), op=Div(), right=Constant(value='speedscope.json')), Constant(value='r')], keywords=[]), optional_vars=Name(id='f', ctx=Store()))], body=[Assign(targets=[Name(id='py_spy_dict', ctx=Store())], value=Call(func=Attribute(value=Name(id='json', ctx=Load()), attr='load', ctx=Load()), args=[Name(id='f', ctx=Load())], keywords=[]))]), Expr(value=Call(func=Name(id='py_spy_to_csv', ctx=Load()), args=[BinOp(left=Name(id='path', ctx=Load()), op=Div(), right=Constant(value='py_spy.csv'))], keywords=[keyword(arg='py_spy_dict', value=Name(id='py_spy_dict', ctx=Load())), keyword(arg='top', value=Attribute(value=Name(id='args', ctx=Load()), attr='top', ctx=Load())), keyword(arg='pattern_to_filter', value=Attribute(value=Name(id='args', ctx=Load()), attr='pattern_to_filter', ctx=Load()))]))], orelse=[])], type_ignores=[])