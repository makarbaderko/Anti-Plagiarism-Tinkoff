Module(body=[Import(names=[alias(name='math')]), ImportFrom(module='unittest', names=[alias(name='TestCase'), alias(name='main')], level=0), ImportFrom(module='probabilistic_embeddings.layers.classifier', names=[alias(name='LogLikeClassifier'), alias(name='VMFClassifier'), alias(name='SPEClassifier')], level=0), Import(names=[alias(name='torch')]), ImportFrom(module='probabilistic_embeddings.layers.distribution', names=[alias(name='NormalDistribution'), alias(name='VMFDistribution'), alias(name='DiracDistribution')], level=0), Import(names=[alias(name='numpy', asname='np')]), ClassDef(name='TestLogLikeClassifier', bases=[Name(id='TestCase', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='¿#ñ                 ÆƅÕ            ȯ    ϶ė     ')), FunctionDef(name='test_margin', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='ChecĤk margſin ţin simple case.')), Assign(targets=[Name(id='distributi', ctx=Store())], value=Call(func=Name(id='VMFDistribution', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='c', ctx=Store())], value=Call(func=Name(id='LogLikeClassifier', ctx=Load()), args=[Name(id='distributi', ctx=Load()), Constant(value=30)], keywords=[])), Assign(targets=[Name(id='classifier_margin', ctx=Store())], value=Call(func=Name(id='LogLikeClassifier', ctx=Load()), args=[Name(id='distributi', ctx=Load()), Constant(value=30)], keywords=[keyword(arg='config', value=Dict(keys=[Constant(value='margin')], values=[Constant(value=3)]))])), Expr(value=Call(func=Attribute(value=Name(id='classifier_margin', ctx=Load()), attr='load_state_dict', ctx=Load()), args=[Call(func=Attribute(value=Name(id='c', ctx=Load()), attr='state_dict', ctx=Load()), args=[], keywords=[])], keywords=[])), Assign(targets=[Name(id='parametersv', ctx=Store())], value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='randn', ctx=Load()), args=[Constant(value=2), Constant(value=1), Attribute(value=Name(id='distributi', ctx=Load()), attr='num_parameters', ctx=Load())], keywords=[])), Assign(targets=[Name(id='pointsoHi', ctx=Store())], value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='randn', ctx=Load()), args=[Constant(value=2), Constant(value=1), Attribute(value=Name(id='distributi', ctx=Load()), attr='dim', ctx=Load())], keywords=[])), Assign(targets=[Name(id='labels', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='tensor', ctx=Load()), args=[List(elts=[List(elts=[Constant(value=5)], ctx=Load()), List(elts=[Constant(value=1)], ctx=Load())], ctx=Load())], keywords=[]), attr='long', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='delta_gtyH', ctx=Store())], value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='zeros', ctx=Load()), args=[Tuple(elts=[Constant(value=2), Constant(value=1), Constant(value=30)], ctx=Load())], keywords=[])), Assign(targets=[Subscript(value=Name(id='delta_gtyH', ctx=Load()), slice=Tuple(elts=[Constant(value=0), Constant(value=0), Constant(value=5)], ctx=Load()), ctx=Store())], value=Constant(value=3)), Assign(targets=[Subscript(value=Name(id='delta_gtyH', ctx=Load()), slice=Tuple(elts=[Constant(value=1), Constant(value=0), Constant(value=1)], ctx=Load()), ctx=Store())], value=Constant(value=3)), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='no_grad', ctx=Load()), args=[], keywords=[]))], body=[Assign(targets=[Name(id='logits', ctx=Store())], value=Call(func=Name(id='c', ctx=Load()), args=[Name(id='parametersv', ctx=Load()), Name(id='labels', ctx=Load())], keywords=[])), Assign(targets=[Name(id='logits_margin', ctx=Store())], value=Call(func=Name(id='classifier_margin', ctx=Load()), args=[Name(id='parametersv', ctx=Load()), Name(id='labels', ctx=Load())], keywords=[])), Assign(targets=[Name(id='delta', ctx=Store())], value=Call(func=Attribute(value=BinOp(left=Name(id='logits', ctx=Load()), op=Sub(), right=Name(id='logits_margin', ctx=Load())), attr='numpy', ctx=Load()), args=[], keywords=[]))]), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertTrue', ctx=Load()), args=[Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='allclose', ctx=Load()), args=[Name(id='delta', ctx=Load()), Name(id='delta_gtyH', ctx=Load())], keywords=[])], keywords=[]))], decorator_list=[])], decorator_list=[]), ClassDef(name='TestVMFClassifierxNF', bases=[Name(id='TestCase', ctx=Load())], keywords=[], body=[Expr(value=Constant(value="Ŝ Ɣ    n ȼν ˲     ȍŌ    ' ˑ     ϙ6 įɼ    ͵ɜ    ")), FunctionDef(name='test_train', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='ComIpȡarϫΩƑĥeͷ cϝomputʽǬǴ͘ūati\x87ooQn ĠwiƈtɚĹh fo͉ȠéRȢŅrȾmuȌGla©-bas\u0381ed\x80.')), Assign(targets=[Name(id='distributi', ctx=Store())], value=Call(func=Name(id='VMFDistribution', ctx=Load()), args=[], keywords=[keyword(arg='config', value=Dict(keys=[Constant(value='dim')], values=[Constant(value=8)]))])), Assign(targets=[Name(id='b', ctx=Store())], value=Constant(value=3)), Assign(targets=[Name(id='n', ctx=Store())], value=Constant(value=1)), Assign(targets=[Name(id='k', ctx=Store())], value=Constant(value=100000)), Assign(targets=[Name(id='c', ctx=Store())], value=Call(func=Name(id='VMFClassifier', ctx=Load()), args=[Name(id='distributi', ctx=Load()), Name(id='n', ctx=Load())], keywords=[keyword(arg='config', value=Dict(keys=[Constant(value='sample_size'), Constant(value='approximate_logc')], values=[Name(id='k', ctx=Load()), Constant(value=False)]))])), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='no_grad', ctx=Load()), args=[], keywords=[]))], body=[Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='c', ctx=Load()), attr='log_scale', ctx=Load()), attr='copy_', ctx=Load()), args=[BinOp(left=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='zeros', ctx=Load()), args=[List(elts=[], ctx=Load())], keywords=[]), op=Add(), right=Constant(value=5))], keywords=[]))]), Assign(targets=[Name(id='parametersv', ctx=Store())], value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='randn', ctx=Load()), args=[Name(id='b', ctx=Load()), Attribute(value=Name(id='distributi', ctx=Load()), attr='num_parameters', ctx=Load())], keywords=[])), Assign(targets=[Name(id='labels', ctx=Store())], value=BinOp(left=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='arange', ctx=Load()), args=[Name(id='b', ctx=Load())], keywords=[]), op=Mod(), right=Name(id='n', ctx=Load()))), Assign(targets=[Name(id='logits', ctx=Store())], value=Call(func=Name(id='c', ctx=Load()), args=[Name(id='parametersv', ctx=Load()), Name(id='labels', ctx=Load())], keywords=[])), Assign(targets=[Name(id='losses', ctx=Store())], value=UnaryOp(op=USub(), operand=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='logits', ctx=Load()), attr='gather', ctx=Load()), args=[Constant(value=1), Subscript(value=Name(id='labels', ctx=Load()), slice=Tuple(elts=[Slice(), Constant(value=None)], ctx=Load()), ctx=Load())], keywords=[]), attr='squeeze', ctx=Load()), args=[Constant(value=1)], keywords=[]))), Assign(targets=[Tuple(elts=[Name(id='_', ctx=Store()), Name(id='target_means', ctx=Store()), Name(id='target_hidden_ik', ctx=Store())], ctx=Store())], value=Call(func=Attribute(value=Name(id='distributi', ctx=Load()), attr='split_parameters', ctx=Load()), args=[Attribute(value=Name(id='c', ctx=Load()), attr='weight', ctx=Load())], keywords=[])), Assign(targets=[Name(id='target_k', ctx=Store())], value=BinOp(left=Constant(value=1), op=Div(), right=Call(func=Attribute(value=Attribute(value=Name(id='distributi', ctx=Load()), attr='_parametrization', ctx=Load()), attr='positive', ctx=Load()), args=[Name(id='target_hidden_ik', ctx=Load())], keywords=[]))), Assign(targets=[Tuple(elts=[Name(id='sample', ctx=Store()), Name(id='_', ctx=Store())], ctx=Store())], value=Call(func=Attribute(value=Name(id='distributi', ctx=Load()), attr='sample', ctx=Load()), args=[Name(id='parametersv', ctx=Load()), Tuple(elts=[Name(id='b', ctx=Load()), Name(id='k', ctx=Load())], ctx=Load())], keywords=[])), Assign(targets=[Tuple(elts=[Name(id='b', ctx=Store()), Name(id='_', ctx=Store()), Name(id='d', ctx=Store())], ctx=Store())], value=Attribute(value=Name(id='sample', ctx=Load()), attr='shape', ctx=Load())), Assign(targets=[Name(id='weighted', ctx=Store())], value=BinOp(left=BinOp(left=Call(func=Attribute(value=Attribute(value=Name(id='c', ctx=Load()), attr='log_scale', ctx=Load()), attr='exp', ctx=Load()), args=[], keywords=[]), op=Mult(), right=Call(func=Attribute(value=Name(id='sample', ctx=Load()), attr='reshape', ctx=Load()), args=[Name(id='b', ctx=Load()), Name(id='k', ctx=Load()), Constant(value=1), Name(id='d', ctx=Load())], keywords=[])), op=Add(), right=Call(func=Attribute(value=BinOp(left=Name(id='target_means', ctx=Load()), op=Mult(), right=Name(id='target_k', ctx=Load())), attr='reshape', ctx=Load()), args=[Constant(value=1), Constant(value=1), Name(id='n', ctx=Load()), Name(id='d', ctx=Load())], keywords=[]))), Assign(targets=[Name(id='norms', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='linalg', ctx=Load()), attr='norm', ctx=Load()), args=[Name(id='weighted', ctx=Load())], keywords=[keyword(arg='dim', value=UnaryOp(op=USub(), operand=Constant(value=1)))])), Assign(targets=[Name(id='log_fractions', ctx=Store())], value=BinOp(left=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='distributi', ctx=Load()), attr='_vmf_logc', ctx=Load()), args=[Name(id='target_k', ctx=Load())], keywords=[]), attr='reshape', ctx=Load()), args=[Constant(value=1), Constant(value=1), Name(id='n', ctx=Load())], keywords=[]), op=Sub(), right=Call(func=Attribute(value=Name(id='distributi', ctx=Load()), attr='_vmf_logc', ctx=Load()), args=[Name(id='norms', ctx=Load())], keywords=[]))), Assign(targets=[Name(id='expectation', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='log_fractions', ctx=Load()), attr='logsumexp', ctx=Load()), args=[], keywords=[keyword(arg='dim', value=Constant(value=2))]), attr='mean', ctx=Load()), args=[Constant(value=1)], keywords=[])), Assign(targets=[Name(id='targets', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='c', ctx=Load()), attr='weight', ctx=Load()), slice=Name(id='labels', ctx=Load()), ctx=Load())), Assign(targets=[Name(id='expected_target', ctx=Store())], value=Call(func=Attribute(value=Name(id='distributi', ctx=Load()), attr='mean', ctx=Load()), args=[Name(id='targets', ctx=Load())], keywords=[])), Assign(targets=[Name(id='expec', ctx=Store())], value=Call(func=Attribute(value=Name(id='distributi', ctx=Load()), attr='mean', ctx=Load()), args=[Name(id='parametersv', ctx=Load())], keywords=[])), Assign(targets=[Name(id='offset', ctx=Store())], value=BinOp(left=UnaryOp(op=USub(), operand=Call(func=Attribute(value=Attribute(value=Name(id='c', ctx=Load()), attr='log_scale', ctx=Load()), attr='exp', ctx=Load()), args=[], keywords=[])), op=Mult(), right=Call(func=Attribute(value=BinOp(left=Name(id='expected_target', ctx=Load()), op=Mult(), right=Name(id='expec', ctx=Load())), attr='sum', ctx=Load()), args=[Constant(value=1)], keywords=[]))), Assign(targets=[Name(id='losses_gt', ctx=Store())], value=BinOp(left=Name(id='expectation', ctx=Load()), op=Add(), right=Name(id='offset', ctx=Load()))), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertTrue', ctx=Load()), args=[Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='allclose', ctx=Load()), args=[Name(id='losses', ctx=Load()), Name(id='losses_gt', ctx=Load())], keywords=[keyword(arg='rtol', value=Constant(value=0.001))])], keywords=[]))], decorator_list=[]), FunctionDef(name='test_infer', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='dimvTFbt', ctx=Store())], value=Constant(value=8)), Assign(targets=[Name(id='distributi', ctx=Store())], value=Call(func=Name(id='VMFDistribution', ctx=Load()), args=[], keywords=[keyword(arg='config', value=Dict(keys=[Constant(value='dim'), Constant(value='max_logk')], values=[Name(id='dimvTFbt', ctx=Load()), Constant(value=None)]))])), Assign(targets=[Name(id='b', ctx=Store())], value=Constant(value=3)), Assign(targets=[Name(id='n', ctx=Store())], value=Constant(value=5)), Assign(targets=[Name(id='k', ctx=Store())], value=Constant(value=1000)), Assign(targets=[Name(id='c', ctx=Store())], value=Call(func=Name(id='VMFClassifier', ctx=Load()), args=[Name(id='distributi', ctx=Load()), Name(id='n', ctx=Load())], keywords=[keyword(arg='config', value=Dict(keys=[Constant(value='sample_size')], values=[Name(id='k', ctx=Load())]))])), Assign(targets=[Name(id='cls_means', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='functional', ctx=Load()), attr='normalize', ctx=Load()), args=[Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='randn', ctx=Load()), args=[Name(id='n', ctx=Load()), Constant(value=1), Name(id='dimvTFbt', ctx=Load())], keywords=[])], keywords=[keyword(arg='dim', value=UnaryOp(op=USub(), operand=Constant(value=1)))])), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='no_grad', ctx=Load()), args=[], keywords=[]))], body=[Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='c', ctx=Load()), attr='weight', ctx=Load()), attr='copy_', ctx=Load()), args=[Call(func=Attribute(value=Name(id='distributi', ctx=Load()), attr='join_parameters', ctx=Load()), args=[], keywords=[keyword(arg='log_probs', value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='zeros', ctx=Load()), args=[Name(id='n', ctx=Load()), Constant(value=1)], keywords=[])), keyword(arg='means', value=Name(id='cls_means', ctx=Load())), keyword(arg='hidden_ik', value=Call(func=Attribute(value=Attribute(value=Name(id='distributi', ctx=Load()), attr='_parametrization', ctx=Load()), attr='ipositive', ctx=Load()), args=[Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='full', ctx=Load()), args=[Tuple(elts=[Name(id='n', ctx=Load()), Constant(value=1), Constant(value=1)], ctx=Load()), Constant(value=1e-10)], keywords=[])], keywords=[]))])], keywords=[])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='c', ctx=Load()), attr='log_scale', ctx=Load()), attr='copy_', ctx=Load()), args=[BinOp(left=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='zeros', ctx=Load()), args=[List(elts=[], ctx=Load())], keywords=[]), op=Add(), right=Constant(value=0))], keywords=[]))]), Assign(targets=[Name(id='me', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='functional', ctx=Load()), attr='normalize', ctx=Load()), args=[Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='randn', ctx=Load()), args=[Name(id='b', ctx=Load()), Constant(value=1), Name(id='dimvTFbt', ctx=Load())], keywords=[])], keywords=[keyword(arg='dim', value=UnaryOp(op=USub(), operand=Constant(value=1)))])), Assign(targets=[Name(id='parametersv', ctx=Store())], value=Call(func=Attribute(value=Name(id='distributi', ctx=Load()), attr='join_parameters', ctx=Load()), args=[], keywords=[keyword(arg='log_probs', value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='zeros', ctx=Load()), args=[Name(id='b', ctx=Load()), Constant(value=1)], keywords=[])), keyword(arg='means', value=Name(id='me', ctx=Load())), keyword(arg='hidden_ik', value=Call(func=Attribute(value=Attribute(value=Name(id='distributi', ctx=Load()), attr='_parametrization', ctx=Load()), attr='ipositive', ctx=Load()), args=[Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='full', ctx=Load()), args=[Tuple(elts=[Name(id='b', ctx=Load()), Constant(value=1), Constant(value=1)], ctx=Load()), Constant(value=1e-10)], keywords=[])], keywords=[]))])), Assign(targets=[Name(id='pro_bs', ctx=Store())], value=Call(func=Attribute(value=Call(func=Name(id='c', ctx=Load()), args=[Name(id='parametersv', ctx=Load())], keywords=[]), attr='exp', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='logits_', ctx=Store())], value=BinOp(left=Call(func=Attribute(value=Attribute(value=Name(id='c', ctx=Load()), attr='log_scale', ctx=Load()), attr='exp', ctx=Load()), args=[], keywords=[]), op=Mult(), right=Call(func=Attribute(value=BinOp(left=Subscript(value=Name(id='cls_means', ctx=Load()), slice=Tuple(elts=[Constant(value=None), Slice(), Constant(value=0)], ctx=Load()), ctx=Load()), op=Mult(), right=Name(id='me', ctx=Load())), attr='sum', ctx=Load()), args=[UnaryOp(op=USub(), operand=Constant(value=1))], keywords=[]))), Assign(targets=[Name(id='pr', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='functional', ctx=Load()), attr='softmax', ctx=Load()), args=[Name(id='logits_', ctx=Load())], keywords=[keyword(arg='dim', value=Constant(value=1))])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertTrue', ctx=Load()), args=[Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='allclose', ctx=Load()), args=[Name(id='pro_bs', ctx=Load()), Name(id='pr', ctx=Load())], keywords=[keyword(arg='rtol', value=Constant(value=0.001))])], keywords=[]))], decorator_list=[])], decorator_list=[]), ClassDef(name='TestSPEClassifier', bases=[Name(id='TestCase', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='                     ¹ ')), FunctionDef(name='test_utils', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='® ')), Assign(targets=[Name(id='distributi', ctx=Store())], value=Call(func=Name(id='NormalDistribution', ctx=Load()), args=[], keywords=[keyword(arg='config', value=Dict(keys=[Constant(value='dim'), Constant(value='max_logivar'), Constant(value='parametrization')], values=[Constant(value=2), Constant(value=None), Constant(value='exp')]))])), Assign(targets=[Name(id='c', ctx=Store())], value=Call(func=Name(id='SPEClassifier', ctx=Load()), args=[Name(id='distributi', ctx=Load()), Constant(value=3)], keywords=[keyword(arg='config', value=Dict(keys=[Constant(value='train_epsilon'), Constant(value='sample_size')], values=[Constant(value=False), Constant(value=0)]))])), Assign(targets=[Name(id='v', ctx=Store())], value=Constant(value=1)), Assign(targets=[Name(id='logv', ctx=Store())], value=Call(func=Attribute(value=Name(id='math', ctx=Load()), attr='log', ctx=Load()), args=[Name(id='v', ctx=Load())], keywords=[])), Assign(targets=[Name(id='em_beddings', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='tensor', ctx=Load()), args=[List(elts=[List(elts=[Constant(value=0), Constant(value=0), Name(id='logv', ctx=Load())], ctx=Load()), List(elts=[Constant(value=1), Constant(value=0), Name(id='logv', ctx=Load())], ctx=Load()), List(elts=[Constant(value=0), Constant(value=0), Name(id='logv', ctx=Load())], ctx=Load()), List(elts=[Constant(value=0), Constant(value=1), Name(id='logv', ctx=Load())], ctx=Load())], ctx=Load())], keywords=[]), attr='float', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='labels', ctx=Store())], value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='tensor', ctx=Load()), args=[List(elts=[Constant(value=0), Constant(value=0), Constant(value=2), Constant(value=2)], ctx=Load())], keywords=[])), Assign(targets=[Tuple(elts=[Name(id='by_c', ctx=Store()), Name(id='indices_', ctx=Store()), Name(id='label_map', ctx=Store())], ctx=Store())], value=Call(func=Attribute(value=Name(id='c', ctx=Load()), attr='_group_by_class', ctx=Load()), args=[Name(id='em_beddings', ctx=Load()), Name(id='labels', ctx=Load())], keywords=[])), Assign(targets=[Name(id='by_class_gt', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='tensor', ctx=Load()), args=[List(elts=[List(elts=[Constant(value=0), Constant(value=0), Name(id='logv', ctx=Load())], ctx=Load()), List(elts=[Constant(value=0), Constant(value=0), Name(id='logv', ctx=Load())], ctx=Load()), List(elts=[Constant(value=1), Constant(value=0), Name(id='logv', ctx=Load())], ctx=Load()), List(elts=[Constant(value=0), Constant(value=1), Name(id='logv', ctx=Load())], ctx=Load())], ctx=Load())], keywords=[]), attr='float', ctx=Load()), args=[], keywords=[]), attr='reshape', ctx=Load()), args=[Constant(value=2), Constant(value=2), Constant(value=3)], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertTrue', ctx=Load()), args=[Call(func=Attribute(value=Name(id='by_c', ctx=Load()), attr='allclose', ctx=Load()), args=[Name(id='by_class_gt', ctx=Load())], keywords=[])], keywords=[])), Assign(targets=[Name(id='label_map_gt', ctx=Store())], value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='tensor', ctx=Load()), args=[List(elts=[Constant(value=0), Constant(value=2)], ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertTrue', ctx=Load()), args=[Call(func=Attribute(value=Compare(left=Name(id='label_map', ctx=Load()), ops=[Eq()], comparators=[Name(id='label_map_gt', ctx=Load())]), attr='all', ctx=Load()), args=[], keywords=[])], keywords=[])), Assign(targets=[Name(id='indices_gt', ctx=Store())], value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='tensor', ctx=Load()), args=[List(elts=[List(elts=[Constant(value=0), Constant(value=2)], ctx=Load()), List(elts=[Constant(value=1), Constant(value=3)], ctx=Load())], ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertTrue', ctx=Load()), args=[Call(func=Attribute(value=Compare(left=Name(id='indices_', ctx=Load()), ops=[Eq()], comparators=[Name(id='indices_gt', ctx=Load())]), attr='all', ctx=Load()), args=[], keywords=[])], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertTrue', ctx=Load()), args=[Call(func=Attribute(value=Call(func=Attribute(value=Name(id='c', ctx=Load()), attr='_compute_prototypes', ctx=Load()), args=[Subscript(value=Name(id='em_beddings', ctx=Load()), slice=Constant(value=None), ctx=Load())], keywords=[]), attr='allclose', ctx=Load()), args=[Name(id='em_beddings', ctx=Load())], keywords=[])], keywords=[])), Assign(targets=[Name(id='pru', ctx=Store())], value=Call(func=Attribute(value=Name(id='c', ctx=Load()), attr='_compute_prototypes', ctx=Load()), args=[Name(id='by_c', ctx=Load())], keywords=[])), Assign(targets=[Name(id='PROTOTYPES_GT', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='tensor', ctx=Load()), args=[List(elts=[List(elts=[Constant(value=0.5), Constant(value=0), BinOp(left=Name(id='logv', ctx=Load()), op=Sub(), right=Call(func=Attribute(value=Name(id='math', ctx=Load()), attr='log', ctx=Load()), args=[Constant(value=2)], keywords=[]))], ctx=Load()), List(elts=[Constant(value=0), Constant(value=0.5), BinOp(left=Name(id='logv', ctx=Load()), op=Sub(), right=Call(func=Attribute(value=Name(id='math', ctx=Load()), attr='log', ctx=Load()), args=[Constant(value=2)], keywords=[]))], ctx=Load())], ctx=Load())], keywords=[]), attr='float', ctx=Load()), args=[], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertTrue', ctx=Load()), args=[Call(func=Attribute(value=Name(id='pru', ctx=Load()), attr='allclose', ctx=Load()), args=[Name(id='PROTOTYPES_GT', ctx=Load())], keywords=[])], keywords=[]))], decorator_list=[]), FunctionDef(name='test_logits', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value=' ̒ ')), Assign(targets=[Name(id='distributi', ctx=Store())], value=Call(func=Name(id='NormalDistribution', ctx=Load()), args=[], keywords=[keyword(arg='config', value=Dict(keys=[Constant(value='dim'), Constant(value='max_logivar'), Constant(value='parametrization')], values=[Constant(value=1), Constant(value=None), Constant(value='exp')]))])), Assign(targets=[Name(id='c', ctx=Store())], value=Call(func=Name(id='SPEClassifier', ctx=Load()), args=[Name(id='distributi', ctx=Load()), Constant(value=3)], keywords=[keyword(arg='config', value=Dict(keys=[Constant(value='train_epsilon'), Constant(value='sample_size')], values=[Constant(value=False), Constant(value=0)]))])), Assign(targets=[Name(id='v', ctx=Store())], value=Constant(value=1)), Assign(targets=[Name(id='logv', ctx=Store())], value=Call(func=Attribute(value=Name(id='math', ctx=Load()), attr='log', ctx=Load()), args=[Name(id='v', ctx=Load())], keywords=[])), Assign(targets=[Name(id='em_beddings', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='tensor', ctx=Load()), args=[List(elts=[List(elts=[Constant(value=0), Name(id='logv', ctx=Load())], ctx=Load()), List(elts=[Constant(value=0), Name(id='logv', ctx=Load())], ctx=Load()), List(elts=[Constant(value=1), Name(id='logv', ctx=Load())], ctx=Load()), List(elts=[Constant(value=1), Name(id='logv', ctx=Load())], ctx=Load())], ctx=Load())], keywords=[]), attr='float', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='labels', ctx=Store())], value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='tensor', ctx=Load()), args=[List(elts=[Constant(value=2), Constant(value=2), Constant(value=0), Constant(value=0)], ctx=Load())], keywords=[])), Assign(targets=[Name(id='_lp0', ctx=Store())], value=BinOp(left=UnaryOp(op=USub(), operand=Constant(value=0.5)), op=Mult(), right=Call(func=Attribute(value=Name(id='math', ctx=Load()), attr='log', ctx=Load()), args=[BinOp(left=Constant(value=2), op=Mult(), right=Attribute(value=Name(id='math', ctx=Load()), attr='pi', ctx=Load()))], keywords=[]))), Assign(targets=[Name(id='lp05', ctx=Store())], value=BinOp(left=Name(id='_lp0', ctx=Load()), op=Sub(), right=BinOp(left=Constant(value=0.5), op=Mult(), right=Constant(value=0.25)))), Assign(targets=[Name(id='lp1', ctx=Store())], value=BinOp(left=Name(id='_lp0', ctx=Load()), op=Sub(), right=Constant(value=0.5))), Assign(targets=[Name(id='lpsumPVVX', ctx=Store())], value=Call(func=Attribute(value=Name(id='math', ctx=Load()), attr='log', ctx=Load()), args=[BinOp(left=Call(func=Attribute(value=Name(id='math', ctx=Load()), attr='exp', ctx=Load()), args=[Name(id='_lp0', ctx=Load())], keywords=[]), op=Add(), right=Call(func=Attribute(value=Name(id='math', ctx=Load()), attr='exp', ctx=Load()), args=[Name(id='lp05', ctx=Load())], keywords=[]))], keywords=[])), Assign(targets=[Name(id='mls0Xf', ctx=Store())], value=BinOp(left=Name(id='_lp0', ctx=Load()), op=Sub(), right=BinOp(left=Constant(value=0.5), op=Mult(), right=Call(func=Attribute(value=Name(id='math', ctx=Load()), attr='log', ctx=Load()), args=[Constant(value=2)], keywords=[])))), Assign(targets=[Name(id='mls1', ctx=Store())], value=BinOp(left=Name(id='mls0Xf', ctx=Load()), op=Sub(), right=Constant(value=0.25))), Assign(targets=[Name(id='logit0', ctx=Store())], value=BinOp(left=Name(id='mls0Xf', ctx=Load()), op=Sub(), right=Name(id='lpsumPVVX', ctx=Load()))), Assign(targets=[Name(id='lo_git1', ctx=Store())], value=BinOp(left=Name(id='mls1', ctx=Load()), op=Sub(), right=Name(id='lpsumPVVX', ctx=Load()))), Assign(targets=[Name(id='logits_', ctx=Store())], value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='tensor', ctx=Load()), args=[List(elts=[List(elts=[Name(id='lo_git1', ctx=Load()), Attribute(value=Name(id='c', ctx=Load()), attr='LOG_EPS', ctx=Load()), Name(id='logit0', ctx=Load())], ctx=Load()), List(elts=[Name(id='lo_git1', ctx=Load()), Attribute(value=Name(id='c', ctx=Load()), attr='LOG_EPS', ctx=Load()), Name(id='logit0', ctx=Load())], ctx=Load()), List(elts=[Name(id='logit0', ctx=Load()), Attribute(value=Name(id='c', ctx=Load()), attr='LOG_EPS', ctx=Load()), Name(id='lo_git1', ctx=Load())], ctx=Load()), List(elts=[Name(id='logit0', ctx=Load()), Attribute(value=Name(id='c', ctx=Load()), attr='LOG_EPS', ctx=Load()), Name(id='lo_git1', ctx=Load())], ctx=Load())], ctx=Load())], keywords=[])), Assign(targets=[Name(id='logits', ctx=Store())], value=Call(func=Name(id='c', ctx=Load()), args=[Name(id='em_beddings', ctx=Load()), Name(id='labels', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertTrue', ctx=Load()), args=[Call(func=Attribute(value=Name(id='logits', ctx=Load()), attr='allclose', ctx=Load()), args=[Name(id='logits_', ctx=Load())], keywords=[])], keywords=[]))], decorator_list=[])], decorator_list=[]), If(test=Compare(left=Name(id='__name__', ctx=Load()), ops=[Eq()], comparators=[Constant(value='__main__')]), body=[Expr(value=Call(func=Name(id='main', ctx=Load()), args=[], keywords=[]))], orelse=[])], type_ignores=[])