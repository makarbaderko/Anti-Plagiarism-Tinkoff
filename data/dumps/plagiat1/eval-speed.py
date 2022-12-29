Module(body=[Import(names=[alias(name='argparse')]), Import(names=[alias(name='os')]), Import(names=[alias(name='tempfile')]), Import(names=[alias(name='time')]), Import(names=[alias(name='numpy', asname='np')]), Import(names=[alias(name='torch')]), ImportFrom(module='tqdm', names=[alias(name='tqdm')], level=0), ImportFrom(module='probabilistic_embeddings.runner', names=[alias(name='Runner')], level=0), FunctionDef(name='PARSE_ARGUMENTS', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='PARSER', ctx=Store())], value=Call(func=Attribute(value=Name(id='argparse', ctx=Load()), attr='ArgumentParser', ctx=Load()), args=[Constant(value='Eval train/inference speed.')], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='PARSER', ctx=Load()), attr='add_argument', ctx=Load()), args=[Constant(value='data')], keywords=[keyword(arg='help', value=Constant(value='Path to dataset root'))])), Expr(value=Call(func=Attribute(value=Name(id='PARSER', ctx=Load()), attr='add_argument', ctx=Load()), args=[Constant(value='--config')], keywords=[keyword(arg='help', value=Constant(value='Path to training config'))])), Return(value=Call(func=Attribute(value=Name(id='PARSER', ctx=Load()), attr='parse_args', ctx=Load()), args=[], keywords=[]))], decorator_list=[]), FunctionDef(name='measure', args=arguments(posonlyargs=[], args=[arg(arg='titl'), arg(arg='fn'), arg(arg='n')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=50)]), body=[Assign(targets=[Name(id='evals', ctx=Store())], value=List(elts=[], ctx=Load())), For(target=Name(id='_', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Name(id='n', ctx=Load())], keywords=[]), body=[Assign(targets=[Name(id='init', ctx=Store())], value=Call(func=Attribute(value=Name(id='time', ctx=Load()), attr='time', ctx=Load()), args=[], keywords=[])), Expr(value=Call(func=Name(id='fn', ctx=Load()), args=[], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='evals', ctx=Load()), attr='append', ctx=Load()), args=[BinOp(left=Call(func=Attribute(value=Name(id='time', ctx=Load()), attr='time', ctx=Load()), args=[], keywords=[]), op=Sub(), right=Name(id='init', ctx=Load()))], keywords=[]))], orelse=[]), Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Call(func=Attribute(value=Constant(value='{}: {:.2f} +- {:.2f} ms'), attr='format', ctx=Load()), args=[Name(id='titl', ctx=Load()), BinOp(left=Constant(value=1000), op=Mult(), right=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='mean', ctx=Load()), args=[Name(id='evals', ctx=Load())], keywords=[])), BinOp(left=Constant(value=1000), op=Mult(), right=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='std', ctx=Load()), args=[Name(id='evals', ctx=Load())], keywords=[]))], keywords=[])], keywords=[]))], decorator_list=[]), FunctionDef(name='main', args=arguments(posonlyargs=[], args=[arg(arg='args')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='tempfile', ctx=Load()), attr='TemporaryDirectory', ctx=Load()), args=[], keywords=[]), optional_vars=Name(id='root', ctx=Store()))], body=[Assign(targets=[Name(id='runner', ctx=Store())], value=Call(func=Name(id='Runner', ctx=Load()), args=[], keywords=[keyword(arg='root', value=Name(id='root', ctx=Load())), keyword(arg='data_root', value=Attribute(value=Name(id='args', ctx=Load()), attr='data', ctx=Load())), keyword(arg='config', value=Attribute(value=Name(id='args', ctx=Load()), attr='config', ctx=Load()))])), Assign(targets=[Attribute(value=Name(id='runner', ctx=Load()), attr='engine', ctx=Store())], value=Call(func=Attribute(value=Name(id='runner', ctx=Load()), attr='get_engine', ctx=Load()), args=[], keywords=[])), Assign(targets=[Attribute(value=Name(id='runner', ctx=Load()), attr='_stage', ctx=Store())], value=Attribute(value=Name(id='runner', ctx=Load()), attr='STAGE_TRAIN', ctx=Load())), Assign(targets=[Attribute(value=Name(id='runner', ctx=Load()), attr='stage_key', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='runner', ctx=Load()), attr='stages', ctx=Load()), slice=UnaryOp(op=USub(), operand=Constant(value=1)), ctx=Load())), Expr(value=Call(func=Attribute(value=Name(id='runner', ctx=Load()), attr='_run_event', ctx=Load()), args=[Constant(value='on_stage_start')], keywords=[])), Assign(targets=[Attribute(value=Name(id='runner', ctx=Load()), attr='callbacks', ctx=Store())], value=DictComp(key=Name(id='K', ctx=Load()), value=Name(id='v', ctx=Load()), generators=[comprehension(target=Tuple(elts=[Name(id='K', ctx=Store()), Name(id='v', ctx=Store())], ctx=Store()), iter=Call(func=Attribute(value=Attribute(value=Name(id='runner', ctx=Load()), attr='callbacks', ctx=Load()), attr='items', ctx=Load()), args=[], keywords=[]), ifs=[Compare(left=Name(id='K', ctx=Load()), ops=[In()], comparators=[List(elts=[Constant(value='criterion'), Constant(value='optimizer')], ctx=Load())])], is_async=0)])), Assign(targets=[Name(id='loa_der', ctx=Store())], value=Subscript(value=Call(func=Attribute(value=Attribute(value=Name(id='runner', ctx=Load()), attr='datasets', ctx=Load()), attr='get_loaders', ctx=Load()), args=[], keywords=[keyword(arg='train', value=Constant(value=True))]), slice=Constant(value='train'), ctx=Load())), Assign(targets=[Tuple(elts=[Name(id='images', ctx=Store()), Name(id='labels', ctx=Store())], ctx=Store())], value=Call(func=Name(id='next', ctx=Load()), args=[Call(func=Name(id='iter', ctx=Load()), args=[Name(id='loa_der', ctx=Load())], keywords=[])], keywords=[])), If(test=Call(func=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='cuda', ctx=Load()), attr='is_available', ctx=Load()), args=[], keywords=[]), body=[Assign(targets=[Name(id='images', ctx=Store())], value=Call(func=Attribute(value=Name(id='images', ctx=Load()), attr='cuda', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='labels', ctx=Store())], value=Call(func=Attribute(value=Name(id='labels', ctx=Load()), attr='cuda', ctx=Load()), args=[], keywords=[]))], orelse=[]), Expr(value=Call(func=Attribute(value=Subscript(value=Attribute(value=Name(id='runner', ctx=Load()), attr='model', ctx=Load()), slice=Constant(value='embedder'), ctx=Load()), attr='train', ctx=Load()), args=[Constant(value=True)], keywords=[])), Expr(value=Call(func=Attribute(value=Call(func=Attribute(value=Call(func=Subscript(value=Attribute(value=Name(id='runner', ctx=Load()), attr='model', ctx=Load()), slice=Constant(value='embedder'), ctx=Load()), args=[Name(id='images', ctx=Load())], keywords=[]), attr='mean', ctx=Load()), args=[], keywords=[]), attr='backward', ctx=Load()), args=[], keywords=[])), Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Constant(value='Memory usage (MB):'), BinOp(left=Call(func=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='cuda', ctx=Load()), attr='max_memory_allocated', ctx=Load()), args=[], keywords=[]), op=Div(), right=BinOp(left=Constant(value=1024), op=Pow(), right=Constant(value=2)))], keywords=[])), Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Constant(value='Memory usage per request (MB):'), BinOp(left=BinOp(left=Call(func=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='cuda', ctx=Load()), attr='max_memory_allocated', ctx=Load()), args=[], keywords=[]), op=Div(), right=BinOp(left=Constant(value=1024), op=Pow(), right=Constant(value=2))), op=Div(), right=Call(func=Name(id='len', ctx=Load()), args=[Name(id='images', ctx=Load())], keywords=[]))], keywords=[])), FunctionDef(name='train__cnn', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Call(func=Attribute(value=Call(func=Attribute(value=Call(func=Subscript(value=Attribute(value=Name(id='runner', ctx=Load()), attr='model', ctx=Load()), slice=Constant(value='embedder'), ctx=Load()), args=[Name(id='images', ctx=Load())], keywords=[]), attr='mean', ctx=Load()), args=[], keywords=[]), attr='backward', ctx=Load()), args=[], keywords=[]))], decorator_list=[]), Expr(value=Call(func=Name(id='measure', ctx=Load()), args=[Constant(value='Train CNN'), Name(id='train__cnn', ctx=Load())], keywords=[])), FunctionDef(name='train_batch', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value=' ɓ¡   Ɯ   ˼  ŀ ɍɫɠ \x96  Ț')), Assign(targets=[Attribute(value=Name(id='runner', ctx=Load()), attr='batch', ctx=Store())], value=Tuple(elts=[Name(id='images', ctx=Load()), Name(id='labels', ctx=Load())], ctx=Load())), Assign(targets=[Attribute(value=Name(id='runner', ctx=Load()), attr='is_train_loader', ctx=Store())], value=Constant(value=True)), Assign(targets=[Attribute(value=Name(id='runner', ctx=Load()), attr='loader_key', ctx=Store())], value=Constant(value='train')), Expr(value=Call(func=Attribute(value=Name(id='runner', ctx=Load()), attr='_run_batch', ctx=Load()), args=[], keywords=[]))], decorator_list=[]), Assign(targets=[Attribute(value=Name(id='runner', ctx=Load()), attr='_stage', ctx=Store())], value=Attribute(value=Name(id='runner', ctx=Load()), attr='STAGE_TEST', ctx=Load())), Assign(targets=[Attribute(value=Name(id='runner', ctx=Load()), attr='stage_key', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='runner', ctx=Load()), attr='stages', ctx=Load()), slice=Constant(value=0), ctx=Load())), Expr(value=Call(func=Attribute(value=Name(id='runner', ctx=Load()), attr='_run_event', ctx=Load()), args=[Constant(value='on_stage_start')], keywords=[])), Assign(targets=[Attribute(value=Name(id='runner', ctx=Load()), attr='callbacks', ctx=Store())], value=DictComp(key=Name(id='K', ctx=Load()), value=Name(id='v', ctx=Load()), generators=[comprehension(target=Tuple(elts=[Name(id='K', ctx=Store()), Name(id='v', ctx=Store())], ctx=Store()), iter=Call(func=Attribute(value=Attribute(value=Name(id='runner', ctx=Load()), attr='callbacks', ctx=Load()), attr='items', ctx=Load()), args=[], keywords=[]), ifs=[Compare(left=Name(id='K', ctx=Load()), ops=[In()], comparators=[List(elts=[Constant(value='criterion')], ctx=Load())])], is_async=0)])), Assign(targets=[Name(id='loa_der', ctx=Store())], value=Subscript(value=Call(func=Attribute(value=Attribute(value=Name(id='runner', ctx=Load()), attr='datasets', ctx=Load()), attr='get_loaders', ctx=Load()), args=[], keywords=[keyword(arg='train', value=Constant(value=False))]), slice=Constant(value='valid'), ctx=Load())), Assign(targets=[Tuple(elts=[Name(id='images', ctx=Store()), Name(id='labels', ctx=Store())], ctx=Store())], value=Call(func=Name(id='next', ctx=Load()), args=[Call(func=Name(id='iter', ctx=Load()), args=[Name(id='loa_der', ctx=Load())], keywords=[])], keywords=[])), If(test=Call(func=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='cuda', ctx=Load()), attr='is_available', ctx=Load()), args=[], keywords=[]), body=[Assign(targets=[Name(id='images', ctx=Store())], value=Call(func=Attribute(value=Name(id='images', ctx=Load()), attr='cuda', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='labels', ctx=Store())], value=Call(func=Attribute(value=Name(id='labels', ctx=Load()), attr='cuda', ctx=Load()), args=[], keywords=[]))], orelse=[]), FunctionDef(name='valid_cnn_', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='    ')), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='no_grad', ctx=Load()), args=[], keywords=[]))], body=[Expr(value=Call(func=Attribute(value=Call(func=Subscript(value=Attribute(value=Name(id='runner', ctx=Load()), attr='model', ctx=Load()), slice=Constant(value='embedder'), ctx=Load()), args=[Call(func=Attribute(value=Name(id='images', ctx=Load()), attr='detach', ctx=Load()), args=[], keywords=[])], keywords=[]), attr='mean', ctx=Load()), args=[], keywords=[]))])], decorator_list=[]), Expr(value=Call(func=Name(id='measure', ctx=Load()), args=[Constant(value='Inference CNN'), Name(id='valid_cnn_', ctx=Load())], keywords=[])), FunctionDef(name='valid_batch', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='    Ǌ     ǃŝ̝   ')), Assign(targets=[Attribute(value=Name(id='runner', ctx=Load()), attr='batch', ctx=Store())], value=Tuple(elts=[Name(id='images', ctx=Load()), Name(id='labels', ctx=Load())], ctx=Load())), Assign(targets=[Attribute(value=Name(id='runner', ctx=Load()), attr='is_train_loader', ctx=Store())], value=Constant(value=False)), Assign(targets=[Attribute(value=Name(id='runner', ctx=Load()), attr='loader_key', ctx=Store())], value=Constant(value='valid')), Expr(value=Call(func=Attribute(value=Name(id='runner', ctx=Load()), attr='_run_batch', ctx=Load()), args=[], keywords=[]))], decorator_list=[]), Expr(value=Call(func=Name(id='measure', ctx=Load()), args=[Constant(value='Inference full'), Name(id='valid_batch', ctx=Load())], keywords=[]))])], decorator_list=[]), If(test=Compare(left=Name(id='__name__', ctx=Load()), ops=[Eq()], comparators=[Constant(value='__main__')]), body=[Assign(targets=[Name(id='args', ctx=Store())], value=Call(func=Name(id='PARSE_ARGUMENTS', ctx=Load()), args=[], keywords=[])), Expr(value=Call(func=Name(id='main', ctx=Load()), args=[Name(id='args', ctx=Load())], keywords=[]))], orelse=[])], type_ignores=[])