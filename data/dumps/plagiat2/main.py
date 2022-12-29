Module(body=[Import(names=[alias(name='subprocess')]), Import(names=[alias(name='pathlib')]), Import(names=[alias(name='json')]), Import(names=[alias(name='threading')]), Import(names=[alias(name='hydra')]), ImportFrom(module='omegaconf', names=[alias(name='DictConfig')], level=0), ImportFrom(module='etna.commands', names=[alias(name='*')], level=0), ImportFrom(module='scripts.utils', names=[alias(name='get_perfomance_dataframe_py_spy')], level=0), Assign(targets=[Name(id='FILE_FOLDER', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Call(func=Attribute(value=Name(id='pathlib', ctx=Load()), attr='Path', ctx=Load()), args=[Name(id='__file__', ctx=Load())], keywords=[]), attr='parent', ctx=Load()), attr='resolve', ctx=Load()), args=[], keywords=[])), FunctionDef(name='output', args=arguments(posonlyargs=[], args=[arg(arg='proc')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[For(target=Name(id='line', ctx=Store()), iter=Call(func=Name(id='ite', ctx=Load()), args=[Attribute(value=Attribute(value=Name(id='proc', ctx=Load()), attr='stdout', ctx=Load()), attr='readline', ctx=Load()), Constant(value=b'')], keywords=[]), body=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Call(func=Attribute(value=Name(id='line', ctx=Load()), attr='decode', ctx=Load()), args=[Constant(value='utf-8')], keywords=[])], keywords=[keyword(arg='end', value=Constant(value=''))]))], orelse=[])], decorator_list=[]), FunctionDef(name='benchtt', args=arguments(posonlyargs=[], args=[arg(arg='cfg', annotation=Name(id='DictConfig', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='     ˎ ł  ϭĪŽ     ș  È ǆ Ǒ')), Assign(targets=[Name(id='proc', ctx=Store())], value=Call(func=Attribute(value=Name(id='subprocess', ctx=Load()), attr='Popen', ctx=Load()), args=[List(elts=[Constant(value='py-spy'), Constant(value='record'), Constant(value='-o'), Constant(value='speedscope.json'), Constant(value='-f'), Constant(value='speedscope'), Constant(value='python'), BinOp(left=BinOp(left=Name(id='FILE_FOLDER', ctx=Load()), op=Div(), right=Constant(value='scripts')), op=Div(), right=Constant(value='run.py'))], ctx=Load())], keywords=[keyword(arg='stdout', value=Attribute(value=Name(id='subprocess', ctx=Load()), attr='PIPE', ctx=Load()))])), Assign(targets=[Name(id='t', ctx=Store())], value=Call(func=Attribute(value=Name(id='threading', ctx=Load()), attr='Thread', ctx=Load()), args=[], keywords=[keyword(arg='target', value=Name(id='output', ctx=Load())), keyword(arg='args', value=Tuple(elts=[Name(id='proc', ctx=Load())], ctx=Load()))])), Expr(value=Call(func=Attribute(value=Name(id='t', ctx=Load()), attr='start', ctx=Load()), args=[], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='proc', ctx=Load()), attr='wait', ctx=Load()), args=[], keywords=[])), With(items=[withitem(context_expr=Call(func=Name(id='open', ctx=Load()), args=[Constant(value='speedscope.json'), Constant(value='r')], keywords=[]), optional_vars=Name(id='_f', ctx=Store()))], body=[Assign(targets=[Name(id='py_spy_dict', ctx=Store())], value=Call(func=Attribute(value=Name(id='json', ctx=Load()), attr='load', ctx=Load()), args=[Name(id='_f', ctx=Load())], keywords=[]))]), Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Name(id='get_perfomance_dataframe_py_spy', ctx=Load()), args=[Name(id='py_spy_dict', ctx=Load())], keywords=[keyword(arg='top', value=Attribute(value=Name(id='cfg', ctx=Load()), attr='top', ctx=Load())), keyword(arg='pattern_to_filter', value=Attribute(value=Name(id='cfg', ctx=Load()), attr='pattern_to_filter', ctx=Load()))])), Assign(targets=[Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='line'), ctx=Store())], value=Call(func=Attribute(value=Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='line'), ctx=Load()), attr='apply', ctx=Load()), args=[Lambda(args=arguments(posonlyargs=[], args=[arg(arg='x')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Attribute(value=Call(func=Attribute(value=Call(func=Name(id='s_tr', ctx=Load()), args=[Name(id='x', ctx=Load())], keywords=[]), attr='strip', ctx=Load()), args=[], keywords=[]), attr='replace', ctx=Load()), args=[Constant(value='\\n'), Constant(value='')], keywords=[]))], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='df', ctx=Load()), attr='to_csv', ctx=Load()), args=[Constant(value='py_spy.csv')], keywords=[]))], decorator_list=[Call(func=Attribute(value=Name(id='hydra', ctx=Load()), attr='main', ctx=Load()), args=[], keywords=[keyword(arg='config_path', value=Constant(value='configs/')), keyword(arg='config_name', value=Constant(value='config'))])], returns=Constant(value=None)), If(test=Compare(left=Name(id='__name__', ctx=Load()), ops=[Eq()], comparators=[Constant(value='__main__')]), body=[Expr(value=Call(func=Name(id='benchtt', ctx=Load()), args=[], keywords=[]))], orelse=[])], type_ignores=[])