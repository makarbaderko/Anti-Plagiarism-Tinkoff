Module(body=[Import(names=[alias(name='json')]), Import(names=[alias(name='pickle')]), Import(names=[alias(name='hydra_slayer')]), Import(names=[alias(name='pytest')]), ImportFrom(module='ruptures', names=[alias(name='Binseg')], level=0), ImportFrom(module='sklearn.linear_model', names=[alias(name='LinearRegression')], level=0), ImportFrom(module='etna.core', names=[alias(name='BaseMixin')], level=0), ImportFrom(module='etna.ensembles', names=[alias(name='StackingEnsemble')], level=0), ImportFrom(module='etna.ensembles', names=[alias(name='VotingEnsemble')], level=0), ImportFrom(module='etna.libs.pytorch_lightning.callbacks', names=[alias(name='EarlyStopping')], level=0), ImportFrom(module='etna.metrics', names=[alias(name='MAE')], level=0), ImportFrom(module='etna.metrics', names=[alias(name='SMAPE')], level=0), ImportFrom(module='etna.models', names=[alias(name='AutoARIMAModel')], level=0), ImportFrom(module='etna.models', names=[alias(name='CatBoostModelPerSegment')], level=0), ImportFrom(module='etna.models', names=[alias(name='LinearPerSegmentModel')], level=0), ImportFrom(module='etna.models.nn', names=[alias(name='DeepARModel')], level=0), ImportFrom(module='etna.models.nn', names=[alias(name='MLPModel')], level=0), ImportFrom(module='etna.pipeline', names=[alias(name='Pipeline')], level=0), ImportFrom(module='etna.transforms', names=[alias(name='AddConstTransform')], level=0), ImportFrom(module='etna.transforms', names=[alias(name='ChangePointsTrendTransform')], level=0), ImportFrom(module='etna.transforms', names=[alias(name='DensityOutliersTransform')], level=0), ImportFrom(module='etna.transforms', names=[alias(name='LambdaTransform')], level=0), ImportFrom(module='etna.transforms', names=[alias(name='LogTransform')], level=0), FunctionDef(name='ensemble_samples', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='pipeline1', ctx=Store())], value=Call(func=Name(id='Pipeline', ctx=Load()), args=[], keywords=[keyword(arg='model', value=Call(func=Name(id='CatBoostModelPerSegment', ctx=Load()), args=[], keywords=[])), keyword(arg='transforms', value=List(elts=[Call(func=Name(id='AddConstTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='value', value=Constant(value=10))]), Call(func=Name(id='ChangePointsTrendTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='change_point_model', value=Call(func=Name(id='Binseg', ctx=Load()), args=[], keywords=[])), keyword(arg='detrend_model', value=Call(func=Name(id='LinearRegression', ctx=Load()), args=[], keywords=[])), keyword(arg='n_bkps', value=Constant(value=50))])], ctx=Load())), keyword(arg='horizon', value=Constant(value=5))])), Assign(targets=[Name(id='pipeline2', ctx=Store())], value=Call(func=Name(id='Pipeline', ctx=Load()), args=[], keywords=[keyword(arg='model', value=Call(func=Name(id='LinearPerSegmentModel', ctx=Load()), args=[], keywords=[])), keyword(arg='transforms', value=List(elts=[Call(func=Name(id='ChangePointsTrendTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='change_point_model', value=Call(func=Name(id='Binseg', ctx=Load()), args=[], keywords=[])), keyword(arg='detrend_model', value=Call(func=Name(id='LinearRegression', ctx=Load()), args=[], keywords=[])), keyword(arg='n_bkps', value=Constant(value=50))]), Call(func=Name(id='LogTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target'))])], ctx=Load())), keyword(arg='horizon', value=Constant(value=5))])), Return(value=List(elts=[Name(id='pipeline1', ctx=Load()), Name(id='pipeline2', ctx=Load())], ctx=Load()))], decorator_list=[]), FunctionDef(name='test_to_dict_transforms', args=arguments(posonlyargs=[], args=[arg(arg='target_object')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='dict_object', ctx=Store())], value=Call(func=Attribute(value=Name(id='target_object', ctx=Load()), attr='to_dict', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='transformed_object', ctx=Store())], value=Call(func=Attribute(value=Name(id='hydra_slayer', ctx=Load()), attr='get_from_params', ctx=Load()), args=[], keywords=[keyword(value=Name(id='dict_object', ctx=Load()))])), Assert(test=Compare(left=Call(func=Attribute(value=Name(id='json', ctx=Load()), attr='loads', ctx=Load()), args=[Call(func=Attribute(value=Name(id='json', ctx=Load()), attr='dumps', ctx=Load()), args=[Name(id='dict_object', ctx=Load())], keywords=[])], keywords=[]), ops=[Eq()], comparators=[Name(id='dict_object', ctx=Load())])), Assert(test=Compare(left=Call(func=Attribute(value=Name(id='pickle', ctx=Load()), attr='dumps', ctx=Load()), args=[Name(id='transformed_object', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Call(func=Attribute(value=Name(id='pickle', ctx=Load()), attr='dumps', ctx=Load()), args=[Name(id='target_object', ctx=Load())], keywords=[])]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='target_object'), List(elts=[Call(func=Name(id='AddConstTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='value', value=Constant(value=10))]), Call(func=Name(id='ChangePointsTrendTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='change_point_model', value=Call(func=Name(id='Binseg', ctx=Load()), args=[], keywords=[])), keyword(arg='detrend_model', value=Call(func=Name(id='LinearRegression', ctx=Load()), args=[], keywords=[])), keyword(arg='n_bkps', value=Constant(value=50))]), Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='param', ctx=Load()), args=[Call(func=Name(id='DensityOutliersTransform', ctx=Load()), args=[Constant(value='target')], keywords=[keyword(arg='distance_coef', value=Constant(value=6))])], keywords=[keyword(arg='marks', value=Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='xfail', ctx=Load()), args=[], keywords=[keyword(arg='reason', value=Constant(value='partial function after initialization instead of original function, dumps return different results'))]))]), Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='param', ctx=Load()), args=[Call(func=Name(id='LambdaTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='transform_func', value=Lambda(args=arguments(posonlyargs=[], args=[arg(arg='x')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=BinOp(left=Name(id='x', ctx=Load()), op=Sub(), right=Constant(value=2)))), keyword(arg='inverse_transform_func', value=Lambda(args=arguments(posonlyargs=[], args=[arg(arg='x')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=BinOp(left=Name(id='x', ctx=Load()), op=Add(), right=Constant(value=2))))])], keywords=[keyword(arg='marks', value=Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='xfail', ctx=Load()), args=[], keywords=[keyword(arg='reason', value=Constant(value='lambdas in class attributes'))]))])], ctx=Load())], keywords=[])]), FunctionDef(name='test_to_dict_transforms_with_expected', args=arguments(posonlyargs=[], args=[arg(arg='target_object'), arg(arg='expected')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='dict_object', ctx=Store())], value=Call(func=Attribute(value=Name(id='target_object', ctx=Load()), attr='to_dict', ctx=Load()), args=[], keywords=[])), Assert(test=Compare(left=Name(id='dict_object', ctx=Load()), ops=[Eq()], comparators=[Name(id='expected', ctx=Load())]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='target_object, expected'), List(elts=[Tuple(elts=[Call(func=Name(id='DensityOutliersTransform', ctx=Load()), args=[Constant(value='target')], keywords=[keyword(arg='distance_coef', value=Constant(value=6))]), Dict(keys=[Constant(value='in_column'), Constant(value='window_size'), Constant(value='distance_coef'), Constant(value='n_neighbors'), Constant(value='distance_func'), Constant(value='_target_')], values=[Constant(value='target'), Constant(value=15), Constant(value=6), Constant(value=3), Dict(keys=[Constant(value='_target_')], values=[Constant(value='etna.analysis.outliers.density_outliers.absolute_difference_distance')]), Constant(value='etna.transforms.outliers.point_outliers.DensityOutliersTransform')])], ctx=Load()), Tuple(elts=[Call(func=Name(id='MLPModel', ctx=Load()), args=[], keywords=[keyword(arg='decoder_length', value=Constant(value=1)), keyword(arg='hidden_size', value=List(elts=[Constant(value=64), Constant(value=64)], ctx=Load())), keyword(arg='input_size', value=Constant(value=1)), keyword(arg='trainer_params', value=Dict(keys=[Constant(value='max_epochs'), Constant(value='callbacks')], values=[Constant(value=100), List(elts=[Call(func=Name(id='EarlyStopping', ctx=Load()), args=[], keywords=[keyword(arg='monitor', value=Constant(value='val_loss')), keyword(arg='patience', value=Constant(value=3))])], ctx=Load())])), keyword(arg='lr', value=Constant(value=0.01)), keyword(arg='train_batch_size', value=Constant(value=32)), keyword(arg='split_params', value=Call(func=Name(id='dict', ctx=Load()), args=[], keywords=[keyword(arg='train_size', value=Constant(value=0.75))]))]), Dict(keys=[Constant(value='input_size'), Constant(value='decoder_length'), Constant(value='hidden_size'), Constant(value='encoder_length'), Constant(value='lr'), Constant(value='train_batch_size'), Constant(value='test_batch_size'), Constant(value='trainer_params'), Constant(value='train_dataloader_params'), Constant(value='test_dataloader_params'), Constant(value='val_dataloader_params'), Constant(value='split_params'), Constant(value='_target_')], values=[Constant(value=1), Constant(value=1), List(elts=[Constant(value=64), Constant(value=64)], ctx=Load()), Constant(value=0), Constant(value=0.01), Constant(value=32), Constant(value=16), Dict(keys=[Constant(value='max_epochs'), Constant(value='callbacks')], values=[Constant(value=100), List(elts=[Dict(keys=[Constant(value='monitor'), Constant(value='patience'), Constant(value='_target_')], values=[Constant(value='val_loss'), Constant(value=3), Constant(value='etna.libs.pytorch_lightning.callbacks.EarlyStopping')])], ctx=Load())]), Dict(keys=[], values=[]), Dict(keys=[], values=[]), Dict(keys=[], values=[]), Dict(keys=[Constant(value='train_size')], values=[Constant(value=0.75)]), Constant(value='etna.models.nn.mlp.MLPModel')])], ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_to_dict_models', args=arguments(posonlyargs=[], args=[arg(arg='target_model')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='dict_object', ctx=Store())], value=Call(func=Attribute(value=Name(id='target_model', ctx=Load()), attr='to_dict', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='transformed_object', ctx=Store())], value=Call(func=Attribute(value=Name(id='hydra_slayer', ctx=Load()), attr='get_from_params', ctx=Load()), args=[], keywords=[keyword(value=Name(id='dict_object', ctx=Load()))])), Assert(test=Compare(left=Call(func=Attribute(value=Name(id='json', ctx=Load()), attr='loads', ctx=Load()), args=[Call(func=Attribute(value=Name(id='json', ctx=Load()), attr='dumps', ctx=Load()), args=[Name(id='dict_object', ctx=Load())], keywords=[])], keywords=[]), ops=[Eq()], comparators=[Name(id='dict_object', ctx=Load())])), Assert(test=Compare(left=Call(func=Attribute(value=Name(id='pickle', ctx=Load()), attr='dumps', ctx=Load()), args=[Name(id='transformed_object', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Call(func=Attribute(value=Name(id='pickle', ctx=Load()), attr='dumps', ctx=Load()), args=[Name(id='target_model', ctx=Load())], keywords=[])]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='target_model'), List(elts=[Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='param', ctx=Load()), args=[Call(func=Name(id='DeepARModel', ctx=Load()), args=[], keywords=[])], keywords=[keyword(arg='marks', value=Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='xfail', ctx=Load()), args=[], keywords=[keyword(arg='reason', value=Constant(value='some bug'))]))]), Call(func=Name(id='LinearPerSegmentModel', ctx=Load()), args=[], keywords=[]), Call(func=Name(id='CatBoostModelPerSegment', ctx=Load()), args=[], keywords=[]), Call(func=Name(id='AutoARIMAModel', ctx=Load()), args=[], keywords=[])], ctx=Load())], keywords=[])]), FunctionDef(name='test_to_dict_pipeline', args=arguments(posonlyargs=[], args=[arg(arg='target_object')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='dict_object', ctx=Store())], value=Call(func=Attribute(value=Name(id='target_object', ctx=Load()), attr='to_dict', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='transformed_object', ctx=Store())], value=Call(func=Attribute(value=Name(id='hydra_slayer', ctx=Load()), attr='get_from_params', ctx=Load()), args=[], keywords=[keyword(value=Name(id='dict_object', ctx=Load()))])), Assert(test=Compare(left=Call(func=Attribute(value=Name(id='json', ctx=Load()), attr='loads', ctx=Load()), args=[Call(func=Attribute(value=Name(id='json', ctx=Load()), attr='dumps', ctx=Load()), args=[Name(id='dict_object', ctx=Load())], keywords=[])], keywords=[]), ops=[Eq()], comparators=[Name(id='dict_object', ctx=Load())])), Assert(test=Compare(left=Call(func=Attribute(value=Name(id='pickle', ctx=Load()), attr='dumps', ctx=Load()), args=[Name(id='transformed_object', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Call(func=Attribute(value=Name(id='pickle', ctx=Load()), attr='dumps', ctx=Load()), args=[Name(id='target_object', ctx=Load())], keywords=[])]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='target_object'), List(elts=[Call(func=Name(id='Pipeline', ctx=Load()), args=[], keywords=[keyword(arg='model', value=Call(func=Name(id='CatBoostModelPerSegment', ctx=Load()), args=[], keywords=[])), keyword(arg='transforms', value=List(elts=[Call(func=Name(id='AddConstTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='value', value=Constant(value=10))]), Call(func=Name(id='ChangePointsTrendTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='change_point_model', value=Call(func=Name(id='Binseg', ctx=Load()), args=[], keywords=[])), keyword(arg='detrend_model', value=Call(func=Name(id='LinearRegression', ctx=Load()), args=[], keywords=[])), keyword(arg='n_bkps', value=Constant(value=50))])], ctx=Load())), keyword(arg='horizon', value=Constant(value=5))])], ctx=Load())], keywords=[])]), FunctionDef(name='test_to_dict_metrics', args=arguments(posonlyargs=[], args=[arg(arg='target_object')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='dict_object', ctx=Store())], value=Call(func=Attribute(value=Name(id='target_object', ctx=Load()), attr='to_dict', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='transformed_object', ctx=Store())], value=Call(func=Attribute(value=Name(id='hydra_slayer', ctx=Load()), attr='get_from_params', ctx=Load()), args=[], keywords=[keyword(value=Name(id='dict_object', ctx=Load()))])), Assert(test=Compare(left=Call(func=Attribute(value=Name(id='json', ctx=Load()), attr='loads', ctx=Load()), args=[Call(func=Attribute(value=Name(id='json', ctx=Load()), attr='dumps', ctx=Load()), args=[Name(id='dict_object', ctx=Load())], keywords=[])], keywords=[]), ops=[Eq()], comparators=[Name(id='dict_object', ctx=Load())])), Assert(test=Compare(left=Call(func=Attribute(value=Name(id='pickle', ctx=Load()), attr='dumps', ctx=Load()), args=[Name(id='transformed_object', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Call(func=Attribute(value=Name(id='pickle', ctx=Load()), attr='dumps', ctx=Load()), args=[Name(id='target_object', ctx=Load())], keywords=[])]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='target_object'), List(elts=[Call(func=Name(id='MAE', ctx=Load()), args=[], keywords=[keyword(arg='mode', value=Constant(value='macro'))]), Call(func=Name(id='SMAPE', ctx=Load()), args=[], keywords=[])], ctx=Load())], keywords=[])]), FunctionDef(name='test_ensembles', args=arguments(posonlyargs=[], args=[arg(arg='target_ensemble')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='dict_object', ctx=Store())], value=Call(func=Attribute(value=Name(id='target_ensemble', ctx=Load()), attr='to_dict', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='transformed_object', ctx=Store())], value=Call(func=Attribute(value=Name(id='hydra_slayer', ctx=Load()), attr='get_from_params', ctx=Load()), args=[], keywords=[keyword(value=Name(id='dict_object', ctx=Load()))])), Assert(test=Compare(left=Call(func=Attribute(value=Name(id='json', ctx=Load()), attr='loads', ctx=Load()), args=[Call(func=Attribute(value=Name(id='json', ctx=Load()), attr='dumps', ctx=Load()), args=[Name(id='dict_object', ctx=Load())], keywords=[])], keywords=[]), ops=[Eq()], comparators=[Name(id='dict_object', ctx=Load())])), Assert(test=Compare(left=Call(func=Attribute(value=Name(id='pickle', ctx=Load()), attr='dumps', ctx=Load()), args=[Name(id='transformed_object', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Call(func=Attribute(value=Name(id='pickle', ctx=Load()), attr='dumps', ctx=Load()), args=[Name(id='target_ensemble', ctx=Load())], keywords=[])]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='target_ensemble'), List(elts=[Call(func=Name(id='VotingEnsemble', ctx=Load()), args=[], keywords=[keyword(arg='pipelines', value=Call(func=Name(id='ensemble_samples', ctx=Load()), args=[], keywords=[])), keyword(arg='weights', value=List(elts=[Constant(value=0.4), Constant(value=0.6)], ctx=Load()))]), Call(func=Name(id='StackingEnsemble', ctx=Load()), args=[], keywords=[keyword(arg='pipelines', value=Call(func=Name(id='ensemble_samples', ctx=Load()), args=[], keywords=[]))])], ctx=Load())], keywords=[])]), ClassDef(name='_Dummy', bases=[], keywords=[], body=[Pass()], decorator_list=[]), ClassDef(name='_InvalidParsing', bases=[Name(id='BaseMixin', ctx=Load())], keywords=[], body=[FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='a', annotation=Name(id='_Dummy', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='a', ctx=Store())], value=Name(id='a', ctx=Load()))], decorator_list=[])], decorator_list=[]), FunctionDef(name='test_warnings', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='warns', ctx=Load()), args=[Name(id='Warning', ctx=Load())], keywords=[keyword(arg='match', value=Constant(value='Some of external objects in input parameters could be not written in dict'))]))], body=[Assign(targets=[Name(id='_', ctx=Store())], value=Call(func=Attribute(value=Call(func=Name(id='_InvalidParsing', ctx=Load()), args=[Call(func=Name(id='_Dummy', ctx=Load()), args=[], keywords=[])], keywords=[]), attr='to_dict', ctx=Load()), args=[], keywords=[]))])], decorator_list=[])], type_ignores=[])