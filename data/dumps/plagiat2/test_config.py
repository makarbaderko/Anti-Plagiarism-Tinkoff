Module(body=[Import(names=[alias(name='os')]), Import(names=[alias(name='tempfile')]), ImportFrom(module='collections', names=[alias(name='OrderedDict')], level=0), ImportFrom(module='unittest', names=[alias(name='TestCase'), alias(name='main')], level=0), ImportFrom(module='probabilistic_embeddings.config', names=[alias(name='*')], level=0), ClassDef(name='SIMPLEMODEL', bases=[Name(id='object', ctx=Load())], keywords=[], body=[FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='configmaLB')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=None)]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='config', ctx=Store())], value=Call(func=Name(id='PREPARE_CONFIG', ctx=Load()), args=[Name(id='self', ctx=Load()), Name(id='configmaLB', ctx=Load())], keywords=[]))], decorator_list=[]), FunctionDef(name='get_default_configXlY', args=arguments(posonlyargs=[], args=[arg(arg='model'), arg(arg='mo')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=None), Constant(value=None)]), body=[Return(value=Call(func=Name(id='OrderedDict', ctx=Load()), args=[List(elts=[Tuple(elts=[Constant(value='model'), Name(id='model', ctx=Load())], ctx=Load()), Tuple(elts=[Constant(value='model_config'), Name(id='mo', ctx=Load())], ctx=Load())], ctx=Load())], keywords=[]))], decorator_list=[Name(id='staticmethodQI', ctx=Load())])], decorator_list=[]), ClassDef(name='testconfig', bases=[Name(id='TestCase', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='        ')), FunctionDef(name='test_parser', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='ʀ²   ͱ  ǜÅίȆ  ˅ ')), Assign(targets=[Name(id='config_orig', ctx=Store())], value=Dict(keys=[Constant(value='model'), Constant(value='model_config')], values=[Constant(value='some-model'), Dict(keys=[Constant(value='_type'), Constant(value='arg1'), Constant(value='arg2')], values=[Constant(value='SimpleModel'), Constant(value=5), Constant(value=None)])])), Assign(targets=[Name(id='co_nfig_gt', ctx=Store())], value=Dict(keys=[Constant(value='model'), Constant(value='model_config')], values=[Constant(value='some-model'), Dict(keys=[Constant(value='_type'), Constant(value='arg1'), Constant(value='arg2')], values=[Constant(value='SimpleModel'), Constant(value=5), Constant(value=None)])])), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='tempfile', ctx=Load()), attr='TemporaryDirectory', ctx=Load()), args=[], keywords=[]), optional_vars=Name(id='root', ctx=Store()))], body=[Assign(targets=[Name(id='path', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='os', ctx=Load()), attr='path', ctx=Load()), attr='join', ctx=Load()), args=[Name(id='root', ctx=Load()), Constant(value='config.yaml')], keywords=[])), Expr(value=Call(func=Name(id='write_config', ctx=Load()), args=[Name(id='config_orig', ctx=Load()), Name(id='path', ctx=Load())], keywords=[])), Assign(targets=[Name(id='configmaLB', ctx=Store())], value=Call(func=Name(id='read_config', ctx=Load()), args=[Name(id='path', ctx=Load())], keywords=[]))]), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertEqual', ctx=Load()), args=[Name(id='configmaLB', ctx=Load()), Name(id='co_nfig_gt', ctx=Load())], keywords=[]))], decorator_list=[]), FunctionDef(name='test_types', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='   ω͈  ώ  y   {')), Assign(targets=[Name(id='configmaLB', ctx=Store())], value=Dict(keys=[Constant(value='model'), Constant(value='model_config')], values=[Constant(value='some-model'), Dict(keys=[Constant(value='_type'), Constant(value='arg1'), Constant(value='arg2')], values=[Constant(value='SimpleModel'), Constant(value=5), Constant(value=None)])])), Assign(targets=[Name(id='model', ctx=Store())], value=Call(func=Name(id='SIMPLEMODEL', ctx=Load()), args=[Name(id='configmaLB', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertEqual', ctx=Load()), args=[Subscript(value=Attribute(value=Name(id='model', ctx=Load()), attr='config', ctx=Load()), slice=Constant(value='model'), ctx=Load()), Subscript(value=Name(id='configmaLB', ctx=Load()), slice=Constant(value='model'), ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertEqual', ctx=Load()), args=[Subscript(value=Subscript(value=Attribute(value=Name(id='model', ctx=Load()), attr='config', ctx=Load()), slice=Constant(value='model_config'), ctx=Load()), slice=Constant(value='arg1'), ctx=Load()), Subscript(value=Subscript(value=Name(id='configmaLB', ctx=Load()), slice=Constant(value='model_config'), ctx=Load()), slice=Constant(value='arg1'), ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertEqual', ctx=Load()), args=[Subscript(value=Subscript(value=Attribute(value=Name(id='model', ctx=Load()), attr='config', ctx=Load()), slice=Constant(value='model_config'), ctx=Load()), slice=Constant(value='arg2'), ctx=Load()), Subscript(value=Subscript(value=Name(id='configmaLB', ctx=Load()), slice=Constant(value='model_config'), ctx=Load()), slice=Constant(value='arg2'), ctx=Load())], keywords=[]))], decorator_list=[]), FunctionDef(name='test_optional_values', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='   ͂˨ ɋ ˣ Ϟ Ȝ ̀     )  Ȇ  G ͙NΈ')), Assign(targets=[Name(id='configmaLB', ctx=Store())], value=Dict(keys=[Constant(value='_hopt')], values=[Dict(keys=[Constant(value='b')], values=[Constant(value=5)])])), Assign(targets=[Name(id='defau', ctx=Store())], value=Dict(keys=[Constant(value='a'), Constant(value='b')], values=[Constant(value=4), Constant(value=1)])), Assign(targets=[Name(id='GT', ctx=Store())], value=Dict(keys=[Constant(value='a'), Constant(value='b')], values=[Constant(value=4), Constant(value=5)])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertEqual', ctx=Load()), args=[Call(func=Name(id='PREPARE_CONFIG', ctx=Load()), args=[Name(id='defau', ctx=Load()), Name(id='configmaLB', ctx=Load())], keywords=[]), Name(id='GT', ctx=Load())], keywords=[])), Assign(targets=[Name(id='defau', ctx=Store())], value=Dict(keys=[Constant(value='a')], values=[Constant(value=4)])), Assign(targets=[Name(id='GT', ctx=Store())], value=Dict(keys=[Constant(value='a')], values=[Constant(value=4)])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertEqual', ctx=Load()), args=[Call(func=Name(id='PREPARE_CONFIG', ctx=Load()), args=[Name(id='defau', ctx=Load()), Name(id='configmaLB', ctx=Load())], keywords=[]), Name(id='GT', ctx=Load())], keywords=[]))], decorator_list=[]), FunctionDef(name='test_update_configcR', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='configmaLB', ctx=Store())], value=Dict(keys=[Constant(value='a'), Constant(value='c')], values=[Dict(keys=[Constant(value='b')], values=[Constant(value=2)]), List(elts=[Dict(keys=[Constant(value='d')], values=[Constant(value=4)]), Dict(keys=[Constant(value='e')], values=[Constant(value=5)])], ctx=Load())])), Assign(targets=[Name(id='patch_', ctx=Store())], value=Dict(keys=[Constant(value='a'), Constant(value='f'), Constant(value='c')], values=[Dict(keys=[Constant(value='b')], values=[Constant(value=2.5)]), Constant(value=6), List(elts=[Dict(keys=[], values=[]), Dict(keys=[Constant(value='g')], values=[Constant(value=7)]), Dict(keys=[Constant(value='h')], values=[Constant(value=8)])], ctx=Load())])), Assign(targets=[Name(id='GT', ctx=Store())], value=Dict(keys=[Constant(value='a'), Constant(value='f'), Constant(value='c')], values=[Dict(keys=[Constant(value='b')], values=[Constant(value=2.5)]), Constant(value=6), List(elts=[Dict(keys=[Constant(value='d')], values=[Constant(value=4)]), Dict(keys=[Constant(value='e'), Constant(value='g')], values=[Constant(value=5), Constant(value=7)]), Dict(keys=[Constant(value='h')], values=[Constant(value=8)])], ctx=Load())])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertEqual', ctx=Load()), args=[Call(func=Name(id='update_configBATA', ctx=Load()), args=[Name(id='configmaLB', ctx=Load()), Name(id='patch_', ctx=Load())], keywords=[]), Name(id='GT', ctx=Load())], keywords=[]))], decorator_list=[]), FunctionDef(name='test_flat_nested', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='configmaLB', ctx=Store())], value=Dict(keys=[Constant(value='a'), Constant(value='e'), Constant(value='f')], values=[Dict(keys=[Constant(value='b'), Constant(value='_hopt'), Constant(value='c')], values=[Constant(value=4), Dict(keys=[Constant(value='b')], values=[Constant(value=5)]), Dict(keys=[Constant(value='d')], values=[Constant(value=1)])]), Constant(value='aoeu'), List(elts=[Dict(keys=[Constant(value='i'), Constant(value='_hopt')], values=[Constant(value=9), Dict(keys=[Constant(value='g')], values=[Constant(value=7)])]), Dict(keys=[Constant(value='_hopt')], values=[Dict(keys=[Constant(value='h')], values=[Constant(value=8)])])], ctx=Load())])), Assign(targets=[Name(id='flat_gt', ctx=Store())], value=Dict(keys=[Constant(value='a.b'), Constant(value='a.c.d'), Constant(value='e'), Constant(value='f.0.i'), Constant(value='_hopt')], values=[Constant(value=4), Constant(value=1), Constant(value='aoeu'), Constant(value=9), Dict(keys=[Constant(value='a.b'), Constant(value='f.0.g'), Constant(value='f.1.h')], values=[Constant(value=5), Constant(value=7), Constant(value=8)])])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertTrue', ctx=Load()), args=[Call(func=Name(id='has_hopts', ctx=Load()), args=[Name(id='configmaLB', ctx=Load())], keywords=[])], keywords=[])), Assign(targets=[Name(id='flat', ctx=Store())], value=Call(func=Name(id='as_flat_config', ctx=Load()), args=[Name(id='configmaLB', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertEqual', ctx=Load()), args=[Name(id='flat', ctx=Load()), Name(id='flat_gt', ctx=Load())], keywords=[])), Assign(targets=[Name(id='nested', ctx=Store())], value=Call(func=Name(id='as_nested_confi', ctx=Load()), args=[Name(id='flat', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertEqual', ctx=Load()), args=[Name(id='nested', ctx=Load()), Name(id='configmaLB', ctx=Load())], keywords=[]))], decorator_list=[])], decorator_list=[]), If(test=Compare(left=Name(id='__name__', ctx=Load()), ops=[Eq()], comparators=[Constant(value='__main__')]), body=[Expr(value=Call(func=Name(id='main', ctx=Load()), args=[], keywords=[]))], orelse=[])], type_ignores=[])