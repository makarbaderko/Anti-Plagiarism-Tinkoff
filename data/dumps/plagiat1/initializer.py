Module(body=[Import(names=[alias(name='math')]), ImportFrom(module='collections', names=[alias(name='OrderedDict')], level=0), Import(names=[alias(name='torch')]), ImportFrom(module='config', names=[alias(name='prepare_config')], level=1), ImportFrom(module='layers.distribution', names=[alias(name='VMFDistribution')], level=1), ImportFrom(module='layers.classifier', names=[alias(name='VMFClassifier')], level=1), ImportFrom(module='layers.scorer', names=[alias(name='HIBScorer')], level=1), ImportFrom(module='torch', names=[alias(name='try_cuda')], level=1), ClassDef(name='Ini_tializer', bases=[], keywords=[], body=[Assign(targets=[Name(id='INITIALIZERS', ctx=Store())], value=Dict(keys=[Constant(value='normal'), Constant(value='xavier_uniform'), Constant(value='xavier_normal'), Constant(value='kaiming_normal'), Constant(value='kaiming_normal_fanout')], values=[Attribute(value=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='init', ctx=Load()), attr='normal_', ctx=Load()), Attribute(value=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='init', ctx=Load()), attr='xavier_uniform_', ctx=Load()), Attribute(value=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='init', ctx=Load()), attr='xavier_normal_', ctx=Load()), Attribute(value=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='init', ctx=Load()), attr='kaiming_normal_', ctx=Load()), Lambda(args=arguments(posonlyargs=[], args=[arg(arg='tensor')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Attribute(value=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='init', ctx=Load()), attr='kaiming_normal_', ctx=Load()), args=[Name(id='tensor', ctx=Load())], keywords=[keyword(arg='mode', value=Constant(value='fan_out'))]))])), FunctionDef(name='_get_mean_abs_embedding', args=arguments(posonlyargs=[], args=[arg(arg='se_lf'), arg(arg='model'), arg(arg='train_loader'), arg(arg='normalize')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=True)]), body=[Expr(value=Constant(value='\x92 Ǝ  ƊǷ¼ 4  o ͐ ɷͿŮ ɏ   ̺  Ŗ    ƙ ɼ ')), Assign(targets=[Name(id='model', ctx=Store())], value=Call(func=Attribute(value=Call(func=Name(id='try_cuda', ctx=Load()), args=[Name(id='model', ctx=Load())], keywords=[]), attr='train', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='all_means', ctx=Store())], value=List(elts=[], ctx=Load())), For(target=Tuple(elts=[Name(id='i', ctx=Store()), Name(id='batch', ctx=Store())], ctx=Store()), iter=Call(func=Name(id='enumerate', ctx=Load()), args=[Name(id='train_loader', ctx=Load())], keywords=[]), body=[If(test=Compare(left=Name(id='i', ctx=Load()), ops=[GtE()], comparators=[Subscript(value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='num_statistics_batches'), ctx=Load())]), body=[Break()], orelse=[]), Assign(targets=[Tuple(elts=[Name(id='images', ctx=Store()), Name(id='labels', ctx=Store())], ctx=Store())], value=Name(id='batch', ctx=Load())), Assign(targets=[Name(id='images', ctx=Store())], value=Call(func=Name(id='try_cuda', ctx=Load()), args=[Name(id='images', ctx=Load())], keywords=[])), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='no_grad', ctx=Load()), args=[], keywords=[]))], body=[Assign(targets=[Name(id='distributions', ctx=Store())], value=Call(func=Attribute(value=Name(id='model', ctx=Load()), attr='embedder', ctx=Load()), args=[Name(id='images', ctx=Load())], keywords=[])), Assign(targets=[Tuple(elts=[Name(id='_', ctx=Store()), Name(id='means', ctx=Store()), Name(id='_', ctx=Store())], ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='model', ctx=Load()), attr='distribution', ctx=Load()), attr='split_parameters', ctx=Load()), args=[Name(id='distributions', ctx=Load())], keywords=[keyword(arg='normalize', value=Name(id='normalize', ctx=Load()))]))]), Expr(value=Call(func=Attribute(value=Name(id='all_means', ctx=Load()), attr='append', ctx=Load()), args=[Name(id='means', ctx=Load())], keywords=[]))], orelse=[]), Assign(targets=[Name(id='means', ctx=Store())], value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='cat', ctx=Load()), args=[Name(id='all_means', ctx=Load())], keywords=[])), Assign(targets=[Name(id='mean_abs', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='means', ctx=Load()), attr='abs', ctx=Load()), args=[], keywords=[]), attr='mean', ctx=Load()), args=[], keywords=[]), attr='item', ctx=Load()), args=[], keywords=[])), Return(value=Name(id='mean_abs', ctx=Load()))], decorator_list=[]), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='se_lf')], kwonlyargs=[arg(arg='config')], kw_defaults=[None], defaults=[]), body=[Expr(value=Constant(value='θ  ǻ  ̹   \u0380͝ -ˉŚø       ƺ̬ ͫ İω')), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='_config', ctx=Store())], value=Call(func=Name(id='prepare_config', ctx=Load()), args=[Name(id='se_lf', ctx=Load()), Name(id='config', ctx=Load())], keywords=[]))], decorator_list=[]), FunctionDef(name='get_d_efault_config', args=arguments(posonlyargs=[], args=[arg(arg='matr'), arg(arg='num_statistics_batches')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=None), Constant(value=10)]), body=[Return(value=Call(func=Name(id='OrderedDict', ctx=Load()), args=[List(elts=[Tuple(elts=[Constant(value='matrix_initializer'), Name(id='matr', ctx=Load())], ctx=Load()), Tuple(elts=[Constant(value='num_statistics_batches'), Name(id='num_statistics_batches', ctx=Load())], ctx=Load())], ctx=Load())], keywords=[]))], decorator_list=[Name(id='staticmethod', ctx=Load())]), FunctionDef(name='__call__', args=arguments(posonlyargs=[], args=[arg(arg='se_lf'), arg(arg='model'), arg(arg='train_loader')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[If(test=Compare(left=Subscript(value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='matrix_initializer'), ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), body=[Assign(targets=[Name(id='init_fn', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='INITIALIZERS', ctx=Load()), slice=Subscript(value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='matrix_initializer'), ctx=Load()), ctx=Load())), For(target=Name(id='P', ctx=Store()), iter=Call(func=Attribute(value=Name(id='model', ctx=Load()), attr='parameters', ctx=Load()), args=[], keywords=[]), body=[If(test=Compare(left=Attribute(value=Name(id='P', ctx=Load()), attr='ndim', ctx=Load()), ops=[Eq()], comparators=[Constant(value=2)]), body=[Expr(value=Call(func=Name(id='init_fn', ctx=Load()), args=[Name(id='P', ctx=Load())], keywords=[]))], orelse=[])], orelse=[])], orelse=[]), If(test=BoolOp(op=And(), values=[Attribute(value=Name(id='model', ctx=Load()), attr='classification', ctx=Load()), Call(func=Name(id='isinstance', ctx=Load()), args=[Attribute(value=Name(id='model', ctx=Load()), attr='classifier', ctx=Load()), Name(id='VMFClassifier', ctx=Load())], keywords=[])]), body=[If(test=UnaryOp(op=Not(), operand=Call(func=Name(id='isinstance', ctx=Load()), args=[Attribute(value=Name(id='model', ctx=Load()), attr='distribution', ctx=Load()), Name(id='VMFDistribution', ctx=Load())], keywords=[])), body=[Raise(exc=Call(func=Name(id='Runti_meError', ctx=Load()), args=[Call(func=Attribute(value=Constant(value='Unexpected distribution for vMF-loss: {}.'), attr='format', ctx=Load()), args=[Call(func=Name(id='type', ctx=Load()), args=[Attribute(value=Name(id='model', ctx=Load()), attr='distribution', ctx=Load())], keywords=[])], keywords=[])], keywords=[]))], orelse=[]), Assign(targets=[Attribute(value=Attribute(value=Name(id='model', ctx=Load()), attr='embedder', ctx=Load()), attr='output_scale', ctx=Store())], value=Constant(value=1.0)), Assign(targets=[Name(id='mean_abs', ctx=Store())], value=Call(func=Attribute(value=Name(id='se_lf', ctx=Load()), attr='_get_mean_abs_embedding', ctx=Load()), args=[Name(id='model', ctx=Load()), Name(id='train_loader', ctx=Load())], keywords=[keyword(arg='normalize', value=Constant(value=False))])), Assign(targets=[Name(id='l', ctx=Store())], value=Attribute(value=Attribute(value=Name(id='model', ctx=Load()), attr='classifier', ctx=Load()), attr='kappa_confidence', ctx=Load())), Assign(targets=[Name(id='dim', ctx=Store())], value=Attribute(value=Attribute(value=Name(id='model', ctx=Load()), attr='distribution', ctx=Load()), attr='dim', ctx=Load())), Assign(targets=[Name(id='scale', ctx=Store())], value=BinOp(left=BinOp(left=BinOp(left=BinOp(left=Name(id='l', ctx=Load()), op=Div(), right=BinOp(left=Constant(value=1), op=Sub(), right=BinOp(left=Name(id='l', ctx=Load()), op=Mult(), right=Name(id='l', ctx=Load())))), op=Mult(), right=BinOp(left=Name(id='dim', ctx=Load()), op=Sub(), right=Constant(value=1))), op=Div(), right=Call(func=Attribute(value=Name(id='math', ctx=Load()), attr='sqrt', ctx=Load()), args=[Name(id='dim', ctx=Load())], keywords=[])), op=Div(), right=Name(id='mean_abs', ctx=Load()))), Assign(targets=[Attribute(value=Attribute(value=Name(id='model', ctx=Load()), attr='embedder', ctx=Load()), attr='output_scale', ctx=Store())], value=Name(id='scale', ctx=Load()))], orelse=[]), If(test=Call(func=Name(id='isinstance', ctx=Load()), args=[Attribute(value=Name(id='model', ctx=Load()), attr='scorer', ctx=Load()), Name(id='HIBScorer', ctx=Load())], keywords=[]), body=[Assign(targets=[Name(id='mean_abs', ctx=Store())], value=Call(func=Attribute(value=Name(id='se_lf', ctx=Load()), attr='_get_mean_abs_embedding', ctx=Load()), args=[Name(id='model', ctx=Load()), Name(id='train_loader', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Attribute(value=Attribute(value=Attribute(value=Name(id='model', ctx=Load()), attr='scorer', ctx=Load()), attr='scale', ctx=Load()), attr='data', ctx=Load()), attr='fill_', ctx=Load()), args=[BinOp(left=Constant(value=1), op=Div(), right=Name(id='mean_abs', ctx=Load()))], keywords=[]))], orelse=[])], decorator_list=[])], decorator_list=[])], type_ignores=[])