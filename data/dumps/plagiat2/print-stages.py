Module(body=[Import(names=[alias(name='argparse')]), ImportFrom(module='probabilistic_embeddings.config', names=[alias(name='read_config'), alias(name='write_config'), alias(name='prepare_config'), alias(name='update_config')], level=0), Import(names=[alias(name='os')]), Import(names=[alias(name='sys')]), Import(names=[alias(name='tempfile')]), ImportFrom(module='probabilistic_embeddings.runner', names=[alias(name='Runner')], level=0), Import(names=[alias(name='copy')]), FunctionDef(name='parse_arguments', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='parser_', ctx=Store())], value=Call(func=Attribute(value=Name(id='argparse', ctx=Load()), attr='ArgumentParser', ctx=Load()), args=[Constant(value='Print configs for all training stages.')], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='parser_', ctx=Load()), attr='add_argument', ctx=Load()), args=[Constant(value='-c'), Constant(value='--config')], keywords=[keyword(arg='help', value=Constant(value='Path to training config.'))])), Expr(value=Call(func=Attribute(value=Name(id='parser_', ctx=Load()), attr='add_argument', ctx=Load()), args=[Constant(value='--hopt')], keywords=[keyword(arg='help', value=Constant(value='Print config for hyper-parameter tuning.')), keyword(arg='action', value=Constant(value='store_true'))])), Return(value=Call(func=Attribute(value=Name(id='parser_', ctx=Load()), attr='parse_args', ctx=Load()), args=[], keywords=[]))], decorator_list=[]), FunctionDef(name='main', args=arguments(posonlyargs=[], args=[arg(arg='args')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='tempfile', ctx=Load()), attr='TemporaryDirectory', ctx=Load()), args=[], keywords=[]), optional_vars=Name(id='root_', ctx=Store()))], body=[Assign(targets=[Name(id='config_', ctx=Store())], value=Attribute(value=Name(id='args', ctx=Load()), attr='config', ctx=Load())), If(test=Attribute(value=Name(id='args', ctx=Load()), attr='hopt', ctx=Load()), body=[Assign(targets=[Name(id='config_', ctx=Store())], value=Call(func=Name(id='prepare_config', ctx=Load()), args=[Name(id='Runner', ctx=Load()), Attribute(value=Name(id='args', ctx=Load()), attr='config', ctx=Load())], keywords=[])), Assign(targets=[Name(id='config_', ctx=Store())], value=Call(func=Name(id='update_config', ctx=Load()), args=[Name(id='config_', ctx=Load()), Subscript(value=Name(id='config_', ctx=Load()), slice=Constant(value='hopt_params'), ctx=Load())], keywords=[]))], orelse=[]), Assign(targets=[Name(id='r', ctx=Store())], value=Call(func=Name(id='Runner', ctx=Load()), args=[], keywords=[keyword(arg='root', value=Name(id='root_', ctx=Load())), keyword(arg='data_root', value=Constant(value=None)), keyword(arg='config', value=Name(id='config_', ctx=Load()))])), Assign(targets=[Attribute(value=Name(id='r', ctx=Load()), attr='_stage', ctx=Store())], value=Attribute(value=Name(id='r', ctx=Load()), attr='STAGE_TRAIN', ctx=Load())), For(target=Name(id='stage', ctx=Store()), iter=Attribute(value=Name(id='r', ctx=Load()), attr='stages', ctx=Load()), body=[Assign(targets=[Name(id='config_', ctx=Store())], value=Call(func=Attribute(value=Name(id='r', ctx=Load()), attr='get_stage_config', ctx=Load()), args=[Name(id='stage', ctx=Load())], keywords=[])), Expr(value=Call(func=Name(id='p', ctx=Load()), args=[Call(func=Attribute(value=Constant(value='=== STAGE {} ==='), attr='format', ctx=Load()), args=[Name(id='stage', ctx=Load())], keywords=[])], keywords=[])), Expr(value=Call(func=Name(id='write_config', ctx=Load()), args=[Name(id='config_', ctx=Load()), Attribute(value=Name(id='sys', ctx=Load()), attr='stdout', ctx=Load())], keywords=[]))], orelse=[])])], decorator_list=[]), If(test=Compare(left=Name(id='__name__', ctx=Load()), ops=[Eq()], comparators=[Constant(value='__main__')]), body=[Assign(targets=[Name(id='args', ctx=Store())], value=Call(func=Name(id='parse_arguments', ctx=Load()), args=[], keywords=[])), Expr(value=Call(func=Name(id='main', ctx=Load()), args=[Name(id='args', ctx=Load())], keywords=[]))], orelse=[])], type_ignores=[])