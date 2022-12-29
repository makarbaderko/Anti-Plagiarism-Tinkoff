Module(body=[ImportFrom(module='os', names=[alias(name='unlink')], level=0), ImportFrom(module='unittest.mock', names=[alias(name='MagicMock')], level=0), ImportFrom(module='unittest.mock', names=[alias(name='patch')], level=0), Import(names=[alias(name='pytest')]), ImportFrom(module='optuna.storages', names=[alias(name='RDBStorage')], level=0), ImportFrom(module='typing_extensions', names=[alias(name='Literal')], level=0), ImportFrom(module='typing_extensions', names=[alias(name='NamedTuple')], level=0), ImportFrom(module='etna.auto', names=[alias(name='Auto')], level=0), ImportFrom(module='etna.auto.auto', names=[alias(name='_Callback')], level=0), ImportFrom(module='etna.auto.auto', names=[alias(name='_Initializer')], level=0), ImportFrom(module='etna.metrics', names=[alias(name='MAE')], level=0), ImportFrom(module='etna.models', names=[alias(name='NaiveModel')], level=0), ImportFrom(module='etna.pipeline', names=[alias(name='Pipeline')], level=0), FunctionDef(name='optuna_storage', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Yield(value=Call(func=Name(id='RDBStorage', ctx=Load()), args=[Constant(value='sqlite:///test.db')], keywords=[]))), Expr(value=Call(func=Name(id='unlink', ctx=Load()), args=[Constant(value='test.db')], keywords=[]))], decorator_list=[Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='fixture', ctx=Load()), args=[], keywords=[])]), FunctionDef(name='trials', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='ƕǴň̚  π ÇE ȏ   ͌ S  ')), ClassDef(name='Trial', bases=[Name(id='NamedTuple', ctx=Load())], keywords=[], body=[Expr(value=Constant(value=' ͌λ      ǃǈ ͑Ď   ȹ  ̝Ƕú̇Ŀ  ʧȼ')), AnnAssign(target=Name(id='user_attrsKsPp', ctx=Store()), annotation=Name(id='dict', ctx=Load()), simple=1), AnnAssign(target=Name(id='state', ctx=Store()), annotation=Subscript(value=Name(id='Literal', ctx=Load()), slice=Tuple(elts=[Constant(value='COMPLETE'), Constant(value='RUNNING'), Constant(value='PENDING')], ctx=Load()), ctx=Load()), value=Constant(value='COMPLETE'), simple=1)], decorator_list=[]), Return(value=ListComp(elt=Call(func=Name(id='Trial', ctx=Load()), args=[], keywords=[keyword(arg='user_attrs', value=Dict(keys=[Constant(value='pipeline'), Constant(value='SMAPE_median')], values=[Call(func=Attribute(value=Name(id='pipeline', ctx=Load()), attr='to_dict', ctx=Load()), args=[], keywords=[]), Name(id='i', ctx=Load())]))]), generators=[comprehension(target=Tuple(elts=[Name(id='i', ctx=Store()), Name(id='pipeline', ctx=Store())], ctx=Store()), iter=Call(func=Name(id='enumerate', ctx=Load()), args=[GeneratorExp(elt=Call(func=Name(id='Pipeline', ctx=Load()), args=[Call(func=Name(id='NaiveModel', ctx=Load()), args=[Name(id='j', ctx=Load())], keywords=[])], keywords=[keyword(arg='horizon', value=Constant(value=7))]), generators=[comprehension(target=Name(id='j', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Constant(value=10)], keywords=[]), ifs=[], is_async=0)])], keywords=[]), ifs=[], is_async=0)]))], decorator_list=[Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='fixture', ctx=Load()), args=[], keywords=[])]), FunctionDef(name='test_objective', args=arguments(posonlyargs=[], args=[arg(arg='example_tsds'), arg(arg='target_metric'), arg(arg='metric_aggregation', annotation=Subscript(value=Name(id='Literal', ctx=Load()), slice=Constant(value='mean'), ctx=Load())), arg(arg='metri'), arg(arg='backtest_params'), arg(arg='initializer'), arg(arg='callback'), arg(arg='relative_params')], kwonlyargs=[], kw_defaults=[], defaults=[Call(func=Name(id='MAE', ctx=Load()), args=[], keywords=[]), Constant(value='mean'), List(elts=[Call(func=Name(id='MAE', ctx=Load()), args=[], keywords=[])], ctx=Load()), Dict(keys=[], values=[]), Call(func=Name(id='MagicMock', ctx=Load()), args=[], keywords=[keyword(arg='spec', value=Name(id='_Initializer', ctx=Load()))]), Call(func=Name(id='MagicMock', ctx=Load()), args=[], keywords=[keyword(arg='spec', value=Name(id='_Callback', ctx=Load()))]), Dict(keys=[Constant(value='_target_'), Constant(value='horizon'), Constant(value='model')], values=[Constant(value='etna.pipeline.Pipeline'), Constant(value=7), Dict(keys=[Constant(value='_target_'), Constant(value='lag')], values=[Constant(value='etna.models.NaiveModel'), Constant(value=1)])])]), body=[Assign(targets=[Name(id='trial', ctx=Store())], value=Call(func=Name(id='MagicMock', ctx=Load()), args=[], keywords=[keyword(arg='relative_params', value=Name(id='relative_params', ctx=Load()))])), Assign(targets=[Name(id='_objective', ctx=Store())], value=Call(func=Attribute(value=Name(id='Auto', ctx=Load()), attr='objective', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='example_tsds', ctx=Load())), keyword(arg='target_metric', value=Name(id='target_metric', ctx=Load())), keyword(arg='metric_aggregation', value=Name(id='metric_aggregation', ctx=Load())), keyword(arg='metrics', value=Name(id='metri', ctx=Load())), keyword(arg='backtest_params', value=Name(id='backtest_params', ctx=Load())), keyword(arg='initializer', value=Name(id='initializer', ctx=Load())), keyword(arg='callback', value=Name(id='callback', ctx=Load()))])), Assign(targets=[Name(id='aggregated_metric', ctx=Store())], value=Call(func=Name(id='_objective', ctx=Load()), args=[Name(id='trial', ctx=Load())], keywords=[])), Assert(test=Call(func=Name(id='isinstance', ctx=Load()), args=[Name(id='aggregated_metric', ctx=Load()), Name(id='float', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='initializer', ctx=Load()), attr='assert_called_once', ctx=Load()), args=[], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='callback', ctx=Load()), attr='assert_called_once', ctx=Load()), args=[], keywords=[]))], decorator_list=[]), FunctionDef(name='test_f', args=arguments(posonlyargs=[], args=[arg(arg='ts'), arg(arg='auto'), arg(arg='timeout_'), arg(arg='n_trials'), arg(arg='initializer'), arg(arg='callback')], kwonlyargs=[], kw_defaults=[], defaults=[Call(func=Name(id='MagicMock', ctx=Load()), args=[], keywords=[]), Call(func=Name(id='MagicMock', ctx=Load()), args=[], keywords=[]), Constant(value=4), Constant(value=2), Call(func=Name(id='MagicMock', ctx=Load()), args=[], keywords=[]), Call(func=Name(id='MagicMock', ctx=Load()), args=[], keywords=[])]), body=[Expr(value=Constant(value='  ʿ ƀs   r ')), Expr(value=Call(func=Attribute(value=Name(id='Auto', ctx=Load()), attr='fit', ctx=Load()), args=[], keywords=[keyword(arg='self', value=Name(id='auto', ctx=Load())), keyword(arg='ts', value=Name(id='ts', ctx=Load())), keyword(arg='timeout', value=Name(id='timeout_', ctx=Load())), keyword(arg='n_trials', value=Name(id='n_trials', ctx=Load())), keyword(arg='initializer', value=Name(id='initializer', ctx=Load())), keyword(arg='callback', value=Name(id='callback', ctx=Load()))])), Expr(value=Call(func=Attribute(value=Attribute(value=Attribute(value=Name(id='auto', ctx=Load()), attr='_optuna', ctx=Load()), attr='tune', ctx=Load()), attr='assert_called_with', ctx=Load()), args=[], keywords=[keyword(arg='objective', value=Attribute(value=Attribute(value=Name(id='auto', ctx=Load()), attr='objective', ctx=Load()), attr='return_value', ctx=Load())), keyword(arg='runner', value=Attribute(value=Name(id='auto', ctx=Load()), attr='runner', ctx=Load())), keyword(arg='n_trials', value=Name(id='n_trials', ctx=Load())), keyword(arg='timeout', value=Name(id='timeout_', ctx=Load()))]))], decorator_list=[]), FunctionDef(name='TEST_INIT_OPTUNA', args=arguments(posonlyargs=[], args=[arg(arg='optuna_mock'), arg(arg='sampler_mock'), arg(arg='auto')], kwonlyargs=[], kw_defaults=[], defaults=[Call(func=Name(id='MagicMock', ctx=Load()), args=[], keywords=[])]), body=[Expr(value=Call(func=Attribute(value=Name(id='Auto', ctx=Load()), attr='_init_optuna', ctx=Load()), args=[], keywords=[keyword(arg='self', value=Name(id='auto', ctx=Load()))])), Expr(value=Call(func=Attribute(value=Name(id='optuna_mock', ctx=Load()), attr='assert_called_once_with', ctx=Load()), args=[], keywords=[keyword(arg='direction', value=Constant(value='maximize')), keyword(arg='study_name', value=Attribute(value=Name(id='auto', ctx=Load()), attr='experiment_folder', ctx=Load())), keyword(arg='storage', value=Attribute(value=Name(id='auto', ctx=Load()), attr='storage', ctx=Load())), keyword(arg='sampler', value=Attribute(value=Name(id='sampler_mock', ctx=Load()), attr='return_value', ctx=Load()))]))], decorator_list=[Call(func=Name(id='patch', ctx=Load()), args=[Constant(value='etna.auto.auto.ConfigSampler')], keywords=[keyword(arg='return_value', value=Call(func=Name(id='MagicMock', ctx=Load()), args=[], keywords=[]))]), Call(func=Name(id='patch', ctx=Load()), args=[Constant(value='etna.auto.auto.Optuna')], keywords=[keyword(arg='return_value', value=Call(func=Name(id='MagicMock', ctx=Load()), args=[], keywords=[]))])]), FunctionDef(name='TEST_SIMPLE_AUTO_RUN', args=arguments(posonlyargs=[], args=[arg(arg='example_tsds'), arg(arg='optuna_storage'), arg(arg='pool')], kwonlyargs=[], kw_defaults=[], defaults=[List(elts=[Call(func=Name(id='Pipeline', ctx=Load()), args=[Call(func=Name(id='NaiveModel', ctx=Load()), args=[Constant(value=1)], keywords=[])], keywords=[keyword(arg='horizon', value=Constant(value=7))]), Call(func=Name(id='Pipeline', ctx=Load()), args=[Call(func=Name(id='NaiveModel', ctx=Load()), args=[Constant(value=50)], keywords=[])], keywords=[keyword(arg='horizon', value=Constant(value=7))])], ctx=Load())]), body=[Assign(targets=[Name(id='auto', ctx=Store())], value=Call(func=Name(id='Auto', ctx=Load()), args=[Call(func=Name(id='MAE', ctx=Load()), args=[], keywords=[])], keywords=[keyword(arg='pool', value=Name(id='pool', ctx=Load())), keyword(arg='metric_aggregation', value=Constant(value='median')), keyword(arg='horizon', value=Constant(value=7)), keyword(arg='storage', value=Name(id='optuna_storage', ctx=Load()))])), Expr(value=Call(func=Attribute(value=Name(id='auto', ctx=Load()), attr='fit', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='example_tsds', ctx=Load())), keyword(arg='n_trials', value=Constant(value=2))])), Assert(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Attribute(value=Attribute(value=Attribute(value=Name(id='auto', ctx=Load()), attr='_optuna', ctx=Load()), attr='study', ctx=Load()), attr='trials', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Constant(value=2)])), Assert(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Call(func=Attribute(value=Name(id='auto', ctx=Load()), attr='summary', ctx=Load()), args=[], keywords=[])], keywords=[]), ops=[Eq()], comparators=[Constant(value=2)])), Assert(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Call(func=Attribute(value=Name(id='auto', ctx=Load()), attr='top_k', ctx=Load()), args=[], keywords=[])], keywords=[]), ops=[Eq()], comparators=[Constant(value=2)])), Assert(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Call(func=Attribute(value=Name(id='auto', ctx=Load()), attr='top_k', ctx=Load()), args=[], keywords=[keyword(arg='k', value=Constant(value=1))])], keywords=[]), ops=[Eq()], comparators=[Constant(value=1)])), Assert(test=Compare(left=Call(func=Name(id='str', ctx=Load()), args=[Subscript(value=Call(func=Attribute(value=Name(id='auto', ctx=Load()), attr='top_k', ctx=Load()), args=[], keywords=[keyword(arg='k', value=Constant(value=1))]), slice=Constant(value=0), ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Call(func=Name(id='str', ctx=Load()), args=[Subscript(value=Name(id='pool', ctx=Load()), slice=Constant(value=0), ctx=Load())], keywords=[])]))], decorator_list=[]), FunctionDef(name='test_summary', args=arguments(posonlyargs=[], args=[arg(arg='trials'), arg(arg='auto')], kwonlyargs=[], kw_defaults=[], defaults=[Call(func=Name(id='MagicMock', ctx=Load()), args=[], keywords=[])]), body=[Assign(targets=[Attribute(value=Attribute(value=Attribute(value=Attribute(value=Name(id='auto', ctx=Load()), attr='_optuna', ctx=Load()), attr='study', ctx=Load()), attr='get_trials', ctx=Load()), attr='return_value', ctx=Store())], value=Name(id='trials', ctx=Load())), Assign(targets=[Name(id='df_summary', ctx=Store())], value=Call(func=Attribute(value=Name(id='Auto', ctx=Load()), attr='summary', ctx=Load()), args=[], keywords=[keyword(arg='self', value=Name(id='auto', ctx=Load()))])), Assert(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Name(id='df_summary', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Call(func=Name(id='len', ctx=Load()), args=[Name(id='trials', ctx=Load())], keywords=[])])), Assert(test=Compare(left=Call(func=Name(id='list', ctx=Load()), args=[Attribute(value=Subscript(value=Name(id='df_summary', ctx=Load()), slice=Constant(value='SMAPE_median'), ctx=Load()), attr='values', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[ListComp(elt=Subscript(value=Attribute(value=Name(id='trial', ctx=Load()), attr='user_attrs', ctx=Load()), slice=Constant(value='SMAPE_median'), ctx=Load()), generators=[comprehension(target=Name(id='trial', ctx=Store()), iter=Name(id='trials', ctx=Load()), ifs=[], is_async=0)])]))], decorator_list=[]), FunctionDef(name='test_top_k', args=arguments(posonlyargs=[], args=[arg(arg='trials'), arg(arg='k'), arg(arg='auto')], kwonlyargs=[], kw_defaults=[], defaults=[Call(func=Name(id='MagicMock', ctx=Load()), args=[], keywords=[])]), body=[Assign(targets=[Attribute(value=Attribute(value=Attribute(value=Attribute(value=Name(id='auto', ctx=Load()), attr='_optuna', ctx=Load()), attr='study', ctx=Load()), attr='get_trials', ctx=Load()), attr='return_value', ctx=Store())], value=Name(id='trials', ctx=Load())), Assign(targets=[Attribute(value=Attribute(value=Name(id='auto', ctx=Load()), attr='target_metric', ctx=Load()), attr='name', ctx=Store())], value=Constant(value='SMAPE')), Assign(targets=[Attribute(value=Name(id='auto', ctx=Load()), attr='metric_aggregation', ctx=Store())], value=Constant(value='median')), Assign(targets=[Attribute(value=Attribute(value=Name(id='auto', ctx=Load()), attr='target_metric', ctx=Load()), attr='greater_is_better', ctx=Store())], value=Constant(value=False)), Assign(targets=[Name(id='df_summary', ctx=Store())], value=Call(func=Attribute(value=Name(id='Auto', ctx=Load()), attr='summary', ctx=Load()), args=[], keywords=[keyword(arg='self', value=Name(id='auto', ctx=Load()))])), Assign(targets=[Attribute(value=Name(id='auto', ctx=Load()), attr='summary', ctx=Store())], value=Call(func=Name(id='MagicMock', ctx=Load()), args=[], keywords=[keyword(arg='return_value', value=Name(id='df_summary', ctx=Load()))])), Assign(targets=[Name(id='top_k', ctx=Store())], value=Call(func=Attribute(value=Name(id='Auto', ctx=Load()), attr='top_k', ctx=Load()), args=[Name(id='auto', ctx=Load())], keywords=[keyword(arg='k', value=Name(id='k', ctx=Load()))])), Assert(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Name(id='top_k', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Name(id='k', ctx=Load())])), Assert(test=Compare(left=ListComp(elt=Attribute(value=Attribute(value=Name(id='pipeline', ctx=Load()), attr='model', ctx=Load()), attr='lag', ctx=Load()), generators=[comprehension(target=Name(id='pipeline', ctx=Store()), iter=Name(id='top_k', ctx=Load()), ifs=[], is_async=0)]), ops=[Eq()], comparators=[ListComp(elt=Name(id='i', ctx=Load()), generators=[comprehension(target=Name(id='i', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Name(id='k', ctx=Load())], keywords=[]), ifs=[], is_async=0)])]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='k'), List(elts=[Constant(value=1), Constant(value=2), Constant(value=3)], ctx=Load())], keywords=[])])], type_ignores=[])