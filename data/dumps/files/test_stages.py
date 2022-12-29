Module(body=[Import(names=[alias(name='os')]), Import(names=[alias(name='sys')]), Import(names=[alias(name='tempfile')]), ImportFrom(module='collections', names=[alias(name='OrderedDict')], level=0), ImportFrom(module='unittest', names=[alias(name='TestCase'), alias(name='main')], level=0), Import(names=[alias(name='numpy', asname='np')]), Import(names=[alias(name='torch')]), Import(names=[alias(name='yaml')]), ImportFrom(module='torchvision', names=[alias(name='transforms')], level=0), ImportFrom(module='probabilistic_embeddings', names=[alias(name='commands')], level=0), ImportFrom(module='probabilistic_embeddings.runner', names=[alias(name='Runner')], level=0), ClassDef(name='Namespace', bases=[], keywords=[], body=[Assign(targets=[Name(id='ARGS', ctx=Store())], value=List(elts=[Constant(value='cmd'), Constant(value='data'), Constant(value='name'), Constant(value='logger'), Constant(value='config'), Constant(value='train_root'), Constant(value='checkpoint'), Constant(value='no_strict_init'), Constant(value='from_stage'), Constant(value='from_seed')], ctx=Load())), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], kwarg=arg(arg='kwargs'), defaults=[]), body=[Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='__dict__', ctx=Load()), attr='update', ctx=Load()), args=[Name(id='kwargs', ctx=Load())], keywords=[]))], decorator_list=[]), FunctionDef(name='__getattr__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='key')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[If(test=Compare(left=Name(id='key', ctx=Load()), ops=[NotIn()], comparators=[Attribute(value=Name(id='self', ctx=Load()), attr='ARGS', ctx=Load())]), body=[Raise(exc=Call(func=Name(id='AttributeError', ctx=Load()), args=[Name(id='key', ctx=Load())], keywords=[]))], orelse=[]), Return(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='__dict__', ctx=Load()), attr='get', ctx=Load()), args=[Name(id='key', ctx=Load()), Constant(value=None)], keywords=[]))], decorator_list=[])], decorator_list=[]), Assign(targets=[Name(id='CONFIG', ctx=Store())], value=Dict(keys=[Constant(value='dataset_params'), Constant(value='model_params'), Constant(value='trainer_params'), Constant(value='num_evaluation_seeds'), Constant(value='stages')], values=[Dict(keys=[Constant(value='name'), Constant(value='batch_size'), Constant(value='num_workers'), Constant(value='num_validation_folds')], values=[Constant(value='debug-openset'), Constant(value=4), Constant(value=0), Constant(value=2)]), Dict(keys=[Constant(value='distribution_type'), Constant(value='distribution_params'), Constant(value='embedder_params'), Constant(value='classifier_type')], values=[Constant(value='vmf'), Dict(keys=[Constant(value='k')], values=[Constant(value='separate')]), Dict(keys=[Constant(value='pretrained'), Constant(value='model_type'), Constant(value='extra_head_dim')], values=[Constant(value=False), Constant(value='resnet18'), Constant(value=1)]), Constant(value='loglike')]), Dict(keys=[Constant(value='num_epochs')], values=[Constant(value=2)]), Constant(value=2), List(elts=[Dict(keys=[Constant(value='model_params')], values=[Dict(keys=[Constant(value='embedder_params')], values=[Dict(keys=[Constant(value='freeze_extra_head')], values=[Constant(value=True)])])]), Dict(keys=[Constant(value='resume_prefixes'), Constant(value='model_params')], values=[Constant(value='_embedder.,_classifier.'), Dict(keys=[Constant(value='freeze_classifier'), Constant(value='embedder_params')], values=[Constant(value=True), Dict(keys=[Constant(value='freeze_stem'), Constant(value='freeze_head'), Constant(value='freeze_normalizer')], values=[Constant(value=True), Constant(value=True), Constant(value=True)])])])], ctx=Load())])), ClassDef(name='TestStages', bases=[Name(id='TestCase', ctx=Load())], keywords=[], body=[FunctionDef(name='test_train', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='tempfile', ctx=Load()), attr='TemporaryDirectory', ctx=Load()), args=[], keywords=[]), optional_vars=Name(id='root', ctx=Store()))], body=[Assign(targets=[Name(id='config', ctx=Store())], value=Call(func=Attribute(value=Name(id='CONFIG', ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='config_path', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='os', ctx=Load()), attr='path', ctx=Load()), attr='join', ctx=Load()), args=[Name(id='root', ctx=Load()), Constant(value='config.yaml')], keywords=[])), With(items=[withitem(context_expr=Call(func=Name(id='open', ctx=Load()), args=[Name(id='config_path', ctx=Load()), Constant(value='w')], keywords=[]), optional_vars=Name(id='fp', ctx=Store()))], body=[Expr(value=Call(func=Attribute(value=Name(id='yaml', ctx=Load()), attr='safe_dump', ctx=Load()), args=[Name(id='config', ctx=Load()), Name(id='fp', ctx=Load())], keywords=[]))]), Assign(targets=[Name(id='args', ctx=Store())], value=Call(func=Name(id='Namespace', ctx=Load()), args=[], keywords=[keyword(arg='cmd', value=Constant(value='train')), keyword(arg='data', value=Name(id='root', ctx=Load())), keyword(arg='config', value=Name(id='config_path', ctx=Load())), keyword(arg='logger', value=Constant(value='tensorboard')), keyword(arg='train_root', value=Name(id='root', ctx=Load()))])), Expr(value=Call(func=Attribute(value=Name(id='commands', ctx=Load()), attr='train', ctx=Load()), args=[Name(id='args', ctx=Load())], keywords=[])), Assign(targets=[Name(id='runner', ctx=Store())], value=Call(func=Name(id='Runner', ctx=Load()), args=[Name(id='root', ctx=Load()), Name(id='root', ctx=Load())], keywords=[keyword(arg='config', value=Name(id='config', ctx=Load()))])), Expr(value=Call(func=Attribute(value=Name(id='runner', ctx=Load()), attr='evaluate', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='checkpoint0', ctx=Store())], value=Call(func=Attribute(value=Subscript(value=Attribute(value=Name(id='runner', ctx=Load()), attr='model', ctx=Load()), slice=Constant(value='model'), ctx=Load()), attr='state_dict', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='checkpoint1', ctx=Store())], value=Subscript(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_load_checkpoint', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='os', ctx=Load()), attr='path', ctx=Load()), attr='join', ctx=Load()), args=[Name(id='root', ctx=Load()), Constant(value='checkpoints'), Constant(value='train-0.')], keywords=[])], keywords=[]), slice=Constant(value='model_model_state_dict'), ctx=Load())), Assign(targets=[Name(id='checkpoint2', ctx=Store())], value=Subscript(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_load_checkpoint', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='os', ctx=Load()), attr='path', ctx=Load()), attr='join', ctx=Load()), args=[Name(id='root', ctx=Load()), Constant(value='checkpoints'), Constant(value='train-1.')], keywords=[])], keywords=[]), slice=Constant(value='model_model_state_dict'), ctx=Load())), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertTrue', ctx=Load()), args=[Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_is_equal', ctx=Load()), args=[Name(id='checkpoint0', ctx=Load()), Name(id='checkpoint1', ctx=Load())], keywords=[keyword(arg='prefix', value=Constant(value='_embedder._extra_head.'))])], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertFalse', ctx=Load()), args=[Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_is_equal', ctx=Load()), args=[Name(id='checkpoint0', ctx=Load()), Name(id='checkpoint1', ctx=Load())], keywords=[keyword(arg='prefix', value=Constant(value='_embedder._stem.'))])], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertFalse', ctx=Load()), args=[Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_is_equal', ctx=Load()), args=[Name(id='checkpoint0', ctx=Load()), Name(id='checkpoint1', ctx=Load())], keywords=[keyword(arg='prefix', value=Constant(value='_embedder._head.'))])], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertFalse', ctx=Load()), args=[Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_is_equal', ctx=Load()), args=[Name(id='checkpoint0', ctx=Load()), Name(id='checkpoint1', ctx=Load())], keywords=[keyword(arg='prefix', value=Constant(value='_embedder._normalizer.'))])], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertFalse', ctx=Load()), args=[Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_is_equal', ctx=Load()), args=[Name(id='checkpoint0', ctx=Load()), Name(id='checkpoint1', ctx=Load())], keywords=[keyword(arg='prefix', value=Constant(value='_classifier.'))])], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertFalse', ctx=Load()), args=[Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_is_equal', ctx=Load()), args=[Name(id='checkpoint1', ctx=Load()), Name(id='checkpoint2', ctx=Load())], keywords=[keyword(arg='prefix', value=Constant(value='_embedder._extra_head.'))])], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertTrue', ctx=Load()), args=[Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_is_equal', ctx=Load()), args=[Name(id='checkpoint1', ctx=Load()), Name(id='checkpoint2', ctx=Load())], keywords=[keyword(arg='prefix', value=Constant(value='_embedder._stem.'))])], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertTrue', ctx=Load()), args=[Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_is_equal', ctx=Load()), args=[Name(id='checkpoint1', ctx=Load()), Name(id='checkpoint2', ctx=Load())], keywords=[keyword(arg='prefix', value=Constant(value='_embedder._head.'))])], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertTrue', ctx=Load()), args=[Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_is_equal', ctx=Load()), args=[Name(id='checkpoint1', ctx=Load()), Name(id='checkpoint2', ctx=Load())], keywords=[keyword(arg='prefix', value=Constant(value='_classifier.'))])], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertTrue', ctx=Load()), args=[Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_is_equal', ctx=Load()), args=[Name(id='checkpoint1', ctx=Load()), Name(id='checkpoint2', ctx=Load())], keywords=[keyword(arg='prefix', value=Constant(value='_embedder._normalizer.'))])], keywords=[]))])], decorator_list=[]), FunctionDef(name='_is_equal', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='state_dict1'), arg(arg='state_dict2'), arg(arg='prefix')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=None)]), body=[If(test=Compare(left=Name(id='prefix', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), body=[Assign(targets=[Name(id='state_dict1', ctx=Store())], value=DictComp(key=Name(id='k', ctx=Load()), value=Name(id='v', ctx=Load()), generators=[comprehension(target=Tuple(elts=[Name(id='k', ctx=Store()), Name(id='v', ctx=Store())], ctx=Store()), iter=Call(func=Attribute(value=Name(id='state_dict1', ctx=Load()), attr='items', ctx=Load()), args=[], keywords=[]), ifs=[Call(func=Attribute(value=Name(id='k', ctx=Load()), attr='startswith', ctx=Load()), args=[Name(id='prefix', ctx=Load())], keywords=[])], is_async=0)])), Assign(targets=[Name(id='state_dict2', ctx=Store())], value=DictComp(key=Name(id='k', ctx=Load()), value=Name(id='v', ctx=Load()), generators=[comprehension(target=Tuple(elts=[Name(id='k', ctx=Store()), Name(id='v', ctx=Store())], ctx=Store()), iter=Call(func=Attribute(value=Name(id='state_dict2', ctx=Load()), attr='items', ctx=Load()), args=[], keywords=[]), ifs=[Call(func=Attribute(value=Name(id='k', ctx=Load()), attr='startswith', ctx=Load()), args=[Name(id='prefix', ctx=Load())], keywords=[])], is_async=0)])), Assert(test=BoolOp(op=And(), values=[Name(id='state_dict1', ctx=Load()), Name(id='state_dict2', ctx=Load())]))], orelse=[]), Assign(targets=[Name(id='is_equal', ctx=Store())], value=Constant(value=True)), If(test=Compare(left=Call(func=Name(id='set', ctx=Load()), args=[Name(id='state_dict1', ctx=Load())], keywords=[]), ops=[NotEq()], comparators=[Call(func=Name(id='set', ctx=Load()), args=[Name(id='state_dict2', ctx=Load())], keywords=[])]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='Keys mismatch')], keywords=[]))], orelse=[]), For(target=Name(id='k', ctx=Store()), iter=Name(id='state_dict1', ctx=Load()), body=[If(test=UnaryOp(op=Not(), operand=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='allclose', ctx=Load()), args=[Call(func=Attribute(value=Call(func=Attribute(value=Subscript(value=Name(id='state_dict1', ctx=Load()), slice=Name(id='k', ctx=Load()), ctx=Load()), attr='cpu', ctx=Load()), args=[], keywords=[]), attr='numpy', ctx=Load()), args=[], keywords=[]), Call(func=Attribute(value=Call(func=Attribute(value=Subscript(value=Name(id='state_dict2', ctx=Load()), slice=Name(id='k', ctx=Load()), ctx=Load()), attr='cpu', ctx=Load()), args=[], keywords=[]), attr='numpy', ctx=Load()), args=[], keywords=[])], keywords=[])), body=[Assign(targets=[Name(id='is_equal', ctx=Store())], value=Constant(value=False)), Break()], orelse=[])], orelse=[]), Return(value=Name(id='is_equal', ctx=Load()))], decorator_list=[]), FunctionDef(name='_load_checkpoint', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='prefix')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='checkpoint', ctx=Store())], value=Constant(value=None)), For(target=Name(id='i', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[BinOp(left=Subscript(value=Subscript(value=Name(id='CONFIG', ctx=Load()), slice=Constant(value='trainer_params'), ctx=Load()), slice=Constant(value='num_epochs'), ctx=Load()), op=Add(), right=Constant(value=1))], keywords=[]), body=[Assign(targets=[Name(id='path', ctx=Store())], value=BinOp(left=BinOp(left=Name(id='prefix', ctx=Load()), op=Add(), right=Call(func=Name(id='str', ctx=Load()), args=[Name(id='i', ctx=Load())], keywords=[])), op=Add(), right=Constant(value='.pth'))), If(test=UnaryOp(op=Not(), operand=Call(func=Attribute(value=Attribute(value=Name(id='os', ctx=Load()), attr='path', ctx=Load()), attr='exists', ctx=Load()), args=[Name(id='path', ctx=Load())], keywords=[])), body=[Continue()], orelse=[]), Return(value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='load', ctx=Load()), args=[Name(id='path', ctx=Load())], keywords=[keyword(arg='map_location', value=Constant(value='cpu'))]))], orelse=[]), Raise(exc=Call(func=Name(id='FileNotFoundError', ctx=Load()), args=[Call(func=Attribute(value=Constant(value='No checkpoint for prefix {}.'), attr='format', ctx=Load()), args=[Name(id='prefix', ctx=Load())], keywords=[])], keywords=[]))], decorator_list=[])], decorator_list=[]), If(test=Compare(left=Name(id='__name__', ctx=Load()), ops=[Eq()], comparators=[Constant(value='__main__')]), body=[Expr(value=Call(func=Name(id='main', ctx=Load()), args=[], keywords=[]))], orelse=[])], type_ignores=[])