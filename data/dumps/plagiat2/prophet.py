Module(body=[ImportFrom(module='datetime', names=[alias(name='datetime')], level=0), ImportFrom(module='typing', names=[alias(name='List')], level=0), ImportFrom(module='etna', names=[alias(name='SETTINGS')], level=0), ImportFrom(module='typing', names=[alias(name='Dict')], level=0), ImportFrom(module='typing', names=[alias(name='Optional')], level=0), ImportFrom(module='typing', names=[alias(name='Sequence')], level=0), ImportFrom(module='typing', names=[alias(name='Union')], level=0), Import(names=[alias(name='pandas', asname='pd')]), ImportFrom(module='etna.models.base', names=[alias(name='BaseAdapter')], level=0), ImportFrom(module='etna.models.mixins', names=[alias(name='PredictionIntervalContextIgnorantModelMixin')], level=0), ImportFrom(module='etna.models.base', names=[alias(name='PredictionIntervalContextIgnorantAbstractModel')], level=0), ImportFrom(module='etna.models.mixins', names=[alias(name='PerSegmentModelMixin')], level=0), ImportFrom(module='typing', names=[alias(name='Iterable')], level=0), If(test=Attribute(value=Name(id='SETTINGS', ctx=Load()), attr='prophet_required', ctx=Load()), body=[ImportFrom(module='prophet', names=[alias(name='Prophet')], level=0)], orelse=[]), ClassDef(name='_ProphetAdap_ter', bases=[Name(id='BaseAdapter', ctx=Load())], keywords=[], body=[Assign(targets=[Name(id='predefined_regressors_names', ctx=Store())], value=Tuple(elts=[Constant(value='floor'), Constant(value='cap')], ctx=Load())), FunctionDef(name='FIT', args=arguments(posonlyargs=[], args=[arg(arg='selfoWj'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), arg(arg='REGRESSORS', annotation=Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='\xadFits a ɔPΜǣſrʩophet modelr.\nΛ\nγParamɖeters\n------Κ--ǰ--ζ\nʴdf:\n ́  ^ Fe%atures qdataframe˥¶\nĉreΟgressors͔:\n  Ȏ  Liİst of th\u0383e co͑lĪʵumns wΎitŜh regƸ̗ressɟʀors')), Assign(targets=[Attribute(value=Name(id='selfoWj', ctx=Load()), attr='regressor_columns', ctx=Store())], value=Name(id='REGRESSORS', ctx=Load())), Assign(targets=[Name(id='prophet_d_f', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), args=[], keywords=[])), Assign(targets=[Subscript(value=Name(id='prophet_d_f', ctx=Load()), slice=Constant(value='y'), ctx=Store())], value=Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='target'), ctx=Load())), Assign(targets=[Subscript(value=Name(id='prophet_d_f', ctx=Load()), slice=Constant(value='ds'), ctx=Store())], value=Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='timestamp'), ctx=Load())), Assign(targets=[Subscript(value=Name(id='prophet_d_f', ctx=Load()), slice=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='regressor_columns', ctx=Load()), ctx=Store())], value=Subscript(value=Name(id='df', ctx=Load()), slice=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='regressor_columns', ctx=Load()), ctx=Load())), For(target=Name(id='regressor', ctx=Store()), iter=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='regressor_columns', ctx=Load()), body=[If(test=Compare(left=Name(id='regressor', ctx=Load()), ops=[NotIn()], comparators=[Attribute(value=Name(id='selfoWj', ctx=Load()), attr='predefined_regressors_names', ctx=Load())]), body=[Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='model', ctx=Load()), attr='add_regressor', ctx=Load()), args=[Name(id='regressor', ctx=Load())], keywords=[]))], orelse=[])], orelse=[]), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='model', ctx=Load()), attr='fit', ctx=Load()), args=[Name(id='prophet_d_f', ctx=Load())], keywords=[])), Return(value=Name(id='selfoWj', ctx=Load()))], decorator_list=[], returns=Constant(value='_ProphetAdapter')), FunctionDef(name='get_model', args=arguments(posonlyargs=[], args=[arg(arg='selfoWj')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='model', ctx=Load()))], decorator_list=[], returns=Name(id='Prophet', ctx=Load())), FunctionDef(name='predict', args=arguments(posonlyargs=[], args=[arg(arg='selfoWj'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), arg(arg='prediction_interval', annotation=Name(id='bool', ctx=Load())), arg(arg='quantiles', annotation=Subscript(value=Name(id='Sequence', ctx=Load()), slice=Name(id='float', ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Name(id='df', ctx=Load()), attr='reset_index', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='prophet_d_f', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), args=[], keywords=[])), Assign(targets=[Subscript(value=Name(id='prophet_d_f', ctx=Load()), slice=Constant(value='y'), ctx=Store())], value=Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='target'), ctx=Load())), Assign(targets=[Subscript(value=Name(id='prophet_d_f', ctx=Load()), slice=Constant(value='ds'), ctx=Store())], value=Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='timestamp'), ctx=Load())), Assign(targets=[Subscript(value=Name(id='prophet_d_f', ctx=Load()), slice=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='regressor_columns', ctx=Load()), ctx=Store())], value=Subscript(value=Name(id='df', ctx=Load()), slice=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='regressor_columns', ctx=Load()), ctx=Load())), Assign(targets=[Name(id='forecast', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='model', ctx=Load()), attr='predict', ctx=Load()), args=[Name(id='prophet_d_f', ctx=Load())], keywords=[])), Assign(targets=[Name(id='y_pred', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), args=[Subscript(value=Name(id='forecast', ctx=Load()), slice=Constant(value='yhat'), ctx=Load())], keywords=[])), If(test=Name(id='prediction_interval', ctx=Load()), body=[Assign(targets=[Name(id='SIM_VALUES', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='model', ctx=Load()), attr='predictive_samples', ctx=Load()), args=[Name(id='prophet_d_f', ctx=Load())], keywords=[])), For(target=Name(id='quantile', ctx=Store()), iter=Name(id='quantiles', ctx=Load()), body=[Assign(targets=[Name(id='percentile', ctx=Store())], value=BinOp(left=Name(id='quantile', ctx=Load()), op=Mult(), right=Constant(value=100))), Assign(targets=[Subscript(value=Name(id='y_pred', ctx=Load()), slice=JoinedStr(values=[Constant(value='yhat_'), FormattedValue(value=Name(id='quantile', ctx=Load()), conversion=-1, format_spec=JoinedStr(values=[Constant(value='.4g')]))]), ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='model', ctx=Load()), attr='percentile', ctx=Load()), args=[Subscript(value=Name(id='SIM_VALUES', ctx=Load()), slice=Constant(value='yhat'), ctx=Load()), Name(id='percentile', ctx=Load())], keywords=[keyword(arg='axis', value=Constant(value=1))]))], orelse=[])], orelse=[]), Assign(targets=[Name(id='rename_dict', ctx=Store())], value=DictComp(key=Name(id='colu', ctx=Load()), value=Call(func=Attribute(value=Name(id='colu', ctx=Load()), attr='replace', ctx=Load()), args=[Constant(value='yhat'), Constant(value='target')], keywords=[]), generators=[comprehension(target=Name(id='colu', ctx=Store()), iter=Attribute(value=Name(id='y_pred', ctx=Load()), attr='columns', ctx=Load()), ifs=[Call(func=Attribute(value=Name(id='colu', ctx=Load()), attr='startswith', ctx=Load()), args=[Constant(value='yhat')], keywords=[])], is_async=0)])), Assign(targets=[Name(id='y_pred', ctx=Store())], value=Call(func=Attribute(value=Name(id='y_pred', ctx=Load()), attr='rename', ctx=Load()), args=[Name(id='rename_dict', ctx=Load())], keywords=[keyword(arg='axis', value=Constant(value=1))])), Return(value=Name(id='y_pred', ctx=Load()))], decorator_list=[], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='selfoWj'), arg(arg='grow_th', annotation=Name(id='str', ctx=Load())), arg(arg='changepoints', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='datetime', ctx=Load()), ctx=Load()), ctx=Load())), arg(arg='n_changepoints', annotation=Name(id='int', ctx=Load())), arg(arg='CHANGEPOINT_RANGE', annotation=Name(id='float', ctx=Load())), arg(arg='yearly_seasonality', annotation=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Name(id='bool', ctx=Load())], ctx=Load()), ctx=Load())), arg(arg='weekly_', annotation=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Name(id='bool', ctx=Load())], ctx=Load()), ctx=Load())), arg(arg='daily_seasonality', annotation=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Name(id='bool', ctx=Load())], ctx=Load()), ctx=Load())), arg(arg='holidays', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), ctx=Load())), arg(arg='seasonality_mode', annotation=Name(id='str', ctx=Load())), arg(arg='seasonality_prior_scale', annotation=Name(id='float', ctx=Load())), arg(arg='holidays_prior_scale', annotation=Name(id='float', ctx=Load())), arg(arg='changepoint_prior_scale', annotation=Name(id='float', ctx=Load())), arg(arg='mcmc_samples', annotation=Name(id='int', ctx=Load())), arg(arg='interval_width', annotation=Name(id='float', ctx=Load())), arg(arg='uncertainty_samples', annotation=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Name(id='int', ctx=Load()), Name(id='bool', ctx=Load())], ctx=Load()), ctx=Load())), arg(arg='stan_backend', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load())), arg(arg='additional_seasonality_params', annotation=Subscript(value=Name(id='Iterable', ctx=Load()), slice=Subscript(value=Name(id='Dict', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Name(id='float', ctx=Load()), Name(id='int', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value='linear'), Constant(value=None), Constant(value=25), Constant(value=0.8), Constant(value='auto'), Constant(value='auto'), Constant(value='auto'), Constant(value=None), Constant(value='additive'), Constant(value=10.0), Constant(value=10.0), Constant(value=0.05), Constant(value=0), Constant(value=0.8), Constant(value=1000), Constant(value=None), Tuple(elts=[], ctx=Load())]), body=[Assign(targets=[Attribute(value=Name(id='selfoWj', ctx=Load()), attr='growth', ctx=Store())], value=Name(id='grow_th', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfoWj', ctx=Load()), attr='n_changepoints', ctx=Store())], value=Name(id='n_changepoints', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfoWj', ctx=Load()), attr='changepoints', ctx=Store())], value=Name(id='changepoints', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfoWj', ctx=Load()), attr='changepoint_range', ctx=Store())], value=Name(id='CHANGEPOINT_RANGE', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfoWj', ctx=Load()), attr='yearly_seasonality', ctx=Store())], value=Name(id='yearly_seasonality', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfoWj', ctx=Load()), attr='weekly_seasonality', ctx=Store())], value=Name(id='weekly_', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfoWj', ctx=Load()), attr='daily_seasonality', ctx=Store())], value=Name(id='daily_seasonality', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfoWj', ctx=Load()), attr='holidays', ctx=Store())], value=Name(id='holidays', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfoWj', ctx=Load()), attr='seasonality_mode', ctx=Store())], value=Name(id='seasonality_mode', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfoWj', ctx=Load()), attr='seasonality_prior_scale', ctx=Store())], value=Name(id='seasonality_prior_scale', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfoWj', ctx=Load()), attr='holidays_prior_scale', ctx=Store())], value=Name(id='holidays_prior_scale', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfoWj', ctx=Load()), attr='changepoint_prior_scale', ctx=Store())], value=Name(id='changepoint_prior_scale', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfoWj', ctx=Load()), attr='mcmc_samples', ctx=Store())], value=Name(id='mcmc_samples', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfoWj', ctx=Load()), attr='interval_width', ctx=Store())], value=Name(id='interval_width', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfoWj', ctx=Load()), attr='uncertainty_samples', ctx=Store())], value=Name(id='uncertainty_samples', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfoWj', ctx=Load()), attr='stan_backend', ctx=Store())], value=Name(id='stan_backend', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfoWj', ctx=Load()), attr='additional_seasonality_params', ctx=Store())], value=Name(id='additional_seasonality_params', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfoWj', ctx=Load()), attr='model', ctx=Store())], value=Call(func=Name(id='Prophet', ctx=Load()), args=[], keywords=[keyword(arg='growth', value=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='growth', ctx=Load())), keyword(arg='changepoints', value=Name(id='changepoints', ctx=Load())), keyword(arg='n_changepoints', value=Name(id='n_changepoints', ctx=Load())), keyword(arg='changepoint_range', value=Name(id='CHANGEPOINT_RANGE', ctx=Load())), keyword(arg='yearly_seasonality', value=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='yearly_seasonality', ctx=Load())), keyword(arg='weekly_seasonality', value=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='weekly_seasonality', ctx=Load())), keyword(arg='daily_seasonality', value=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='daily_seasonality', ctx=Load())), keyword(arg='holidays', value=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='holidays', ctx=Load())), keyword(arg='seasonality_mode', value=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='seasonality_mode', ctx=Load())), keyword(arg='seasonality_prior_scale', value=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='seasonality_prior_scale', ctx=Load())), keyword(arg='holidays_prior_scale', value=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='holidays_prior_scale', ctx=Load())), keyword(arg='changepoint_prior_scale', value=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='changepoint_prior_scale', ctx=Load())), keyword(arg='mcmc_samples', value=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='mcmc_samples', ctx=Load())), keyword(arg='interval_width', value=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='interval_width', ctx=Load())), keyword(arg='uncertainty_samples', value=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='uncertainty_samples', ctx=Load())), keyword(arg='stan_backend', value=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='stan_backend', ctx=Load()))])), For(target=Name(id='seasonality_params', ctx=Store()), iter=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='additional_seasonality_params', ctx=Load()), body=[Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='model', ctx=Load()), attr='add_seasonality', ctx=Load()), args=[], keywords=[keyword(value=Name(id='seasonality_params', ctx=Load()))]))], orelse=[]), AnnAssign(target=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='regressor_columns', ctx=Store()), annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load()), ctx=Load()), value=Constant(value=None), simple=0)], decorator_list=[])], decorator_list=[]), ClassDef(name='ProphetModel', bases=[Name(id='PerSegmentModelMixin', ctx=Load()), Name(id='PredictionIntervalContextIgnorantModelMixin', ctx=Load()), Name(id='PredictionIntervalContextIgnorantAbstractModel', ctx=Load())], keywords=[], body=[FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='selfoWj'), arg(arg='grow_th', annotation=Name(id='str', ctx=Load())), arg(arg='changepoints', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='datetime', ctx=Load()), ctx=Load()), ctx=Load())), arg(arg='n_changepoints', annotation=Name(id='int', ctx=Load())), arg(arg='CHANGEPOINT_RANGE', annotation=Name(id='float', ctx=Load())), arg(arg='yearly_seasonality', annotation=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Name(id='bool', ctx=Load())], ctx=Load()), ctx=Load())), arg(arg='weekly_', annotation=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Name(id='bool', ctx=Load())], ctx=Load()), ctx=Load())), arg(arg='daily_seasonality', annotation=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Name(id='bool', ctx=Load())], ctx=Load()), ctx=Load())), arg(arg='holidays', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), ctx=Load())), arg(arg='seasonality_mode', annotation=Name(id='str', ctx=Load())), arg(arg='seasonality_prior_scale', annotation=Name(id='float', ctx=Load())), arg(arg='holidays_prior_scale', annotation=Name(id='float', ctx=Load())), arg(arg='changepoint_prior_scale', annotation=Name(id='float', ctx=Load())), arg(arg='mcmc_samples', annotation=Name(id='int', ctx=Load())), arg(arg='interval_width', annotation=Name(id='float', ctx=Load())), arg(arg='uncertainty_samples', annotation=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Name(id='int', ctx=Load()), Name(id='bool', ctx=Load())], ctx=Load()), ctx=Load())), arg(arg='stan_backend', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load())), arg(arg='additional_seasonality_params', annotation=Subscript(value=Name(id='Iterable', ctx=Load()), slice=Subscript(value=Name(id='Dict', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Name(id='float', ctx=Load()), Name(id='int', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value='linear'), Constant(value=None), Constant(value=25), Constant(value=0.8), Constant(value='auto'), Constant(value='auto'), Constant(value='auto'), Constant(value=None), Constant(value='additive'), Constant(value=10.0), Constant(value=10.0), Constant(value=0.05), Constant(value=0), Constant(value=0.8), Constant(value=1000), Constant(value=None), Tuple(elts=[], ctx=Load())]), body=[Assign(targets=[Attribute(value=Name(id='selfoWj', ctx=Load()), attr='growth', ctx=Store())], value=Name(id='grow_th', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfoWj', ctx=Load()), attr='n_changepoints', ctx=Store())], value=Name(id='n_changepoints', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfoWj', ctx=Load()), attr='changepoints', ctx=Store())], value=Name(id='changepoints', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfoWj', ctx=Load()), attr='changepoint_range', ctx=Store())], value=Name(id='CHANGEPOINT_RANGE', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfoWj', ctx=Load()), attr='yearly_seasonality', ctx=Store())], value=Name(id='yearly_seasonality', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfoWj', ctx=Load()), attr='weekly_seasonality', ctx=Store())], value=Name(id='weekly_', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfoWj', ctx=Load()), attr='daily_seasonality', ctx=Store())], value=Name(id='daily_seasonality', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfoWj', ctx=Load()), attr='holidays', ctx=Store())], value=Name(id='holidays', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfoWj', ctx=Load()), attr='seasonality_mode', ctx=Store())], value=Name(id='seasonality_mode', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfoWj', ctx=Load()), attr='seasonality_prior_scale', ctx=Store())], value=Name(id='seasonality_prior_scale', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfoWj', ctx=Load()), attr='holidays_prior_scale', ctx=Store())], value=Name(id='holidays_prior_scale', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfoWj', ctx=Load()), attr='changepoint_prior_scale', ctx=Store())], value=Name(id='changepoint_prior_scale', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfoWj', ctx=Load()), attr='mcmc_samples', ctx=Store())], value=Name(id='mcmc_samples', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfoWj', ctx=Load()), attr='interval_width', ctx=Store())], value=Name(id='interval_width', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfoWj', ctx=Load()), attr='uncertainty_samples', ctx=Store())], value=Name(id='uncertainty_samples', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfoWj', ctx=Load()), attr='stan_backend', ctx=Store())], value=Name(id='stan_backend', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfoWj', ctx=Load()), attr='additional_seasonality_params', ctx=Store())], value=Name(id='additional_seasonality_params', ctx=Load())), Expr(value=Call(func=Attribute(value=Call(func=Name(id='SUPER', ctx=Load()), args=[Name(id='ProphetModel', ctx=Load()), Name(id='selfoWj', ctx=Load())], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[keyword(arg='base_model', value=Call(func=Name(id='_ProphetAdap_ter', ctx=Load()), args=[], keywords=[keyword(arg='growth', value=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='growth', ctx=Load())), keyword(arg='n_changepoints', value=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='n_changepoints', ctx=Load())), keyword(arg='changepoints', value=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='changepoints', ctx=Load())), keyword(arg='changepoint_range', value=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='changepoint_range', ctx=Load())), keyword(arg='yearly_seasonality', value=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='yearly_seasonality', ctx=Load())), keyword(arg='weekly_seasonality', value=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='weekly_seasonality', ctx=Load())), keyword(arg='daily_seasonality', value=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='daily_seasonality', ctx=Load())), keyword(arg='holidays', value=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='holidays', ctx=Load())), keyword(arg='seasonality_mode', value=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='seasonality_mode', ctx=Load())), keyword(arg='seasonality_prior_scale', value=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='seasonality_prior_scale', ctx=Load())), keyword(arg='holidays_prior_scale', value=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='holidays_prior_scale', ctx=Load())), keyword(arg='changepoint_prior_scale', value=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='changepoint_prior_scale', ctx=Load())), keyword(arg='mcmc_samples', value=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='mcmc_samples', ctx=Load())), keyword(arg='interval_width', value=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='interval_width', ctx=Load())), keyword(arg='uncertainty_samples', value=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='uncertainty_samples', ctx=Load())), keyword(arg='stan_backend', value=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='stan_backend', ctx=Load())), keyword(arg='additional_seasonality_params', value=Attribute(value=Name(id='selfoWj', ctx=Load()), attr='additional_seasonality_params', ctx=Load()))]))]))], decorator_list=[])], decorator_list=[])], type_ignores=[])