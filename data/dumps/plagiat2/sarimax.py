Module(body=[Import(names=[alias(name='warnings')]), ImportFrom(module='abc', names=[alias(name='abstractmethod')], level=0), ImportFrom(module='typing', names=[alias(name='Sequence')], level=0), ImportFrom(module='typing', names=[alias(name='List')], level=0), ImportFrom(module='etna.libs.pmdarima_utils', names=[alias(name='seasonal_prediction_with_confidence')], level=0), ImportFrom(module='statsmodels.tsa.statespace.sarimax', names=[alias(name='SARIMAXResultsWrapper')], level=0), ImportFrom(module='datetime', names=[alias(name='datetime')], level=0), Import(names=[alias(name='pandas', asname='pd')]), ImportFrom(module='statsmodels.tools.sm_exceptions', names=[alias(name='ValueWarning')], level=0), ImportFrom(module='statsmodels.tsa.statespace.sarimax', names=[alias(name='SARIMAX')], level=0), ImportFrom(module='typing', names=[alias(name='Optional')], level=0), ImportFrom(module='etna.models.base', names=[alias(name='BaseAdapter')], level=0), ImportFrom(module='typing', names=[alias(name='Tuple')], level=0), ImportFrom(module='etna.models.base', names=[alias(name='PredictionIntervalContextIgnorantAbstractModel')], level=0), ImportFrom(module='etna.models.mixins', names=[alias(name='PerSegmentModelMixin')], level=0), ImportFrom(module='etna.models.mixins', names=[alias(name='PredictionIntervalContextIgnorantModelMixin')], level=0), ImportFrom(module='etna.models.utils', names=[alias(name='determine_num_steps')], level=0), Expr(value=Call(func=Attribute(value=Name(id='warnings', ctx=Load()), attr='filterwarnings', ctx=Load()), args=[], keywords=[keyword(arg='message', value=Constant(value='No frequency information was provided, so inferred frequency .* will be used')), keyword(arg='action', value=Constant(value='ignore')), keyword(arg='category', value=Name(id='ValueWarning', ctx=Load())), keyword(arg='module', value=Constant(value='statsmodels.tsa.base.tsa_model'))])), ClassDef(name='_SARIMAXBaseAdapter', bases=[Name(id='BaseAdapter', ctx=Load())], keywords=[], body=[FunctionDef(name='_select_regressorsK', args=arguments(posonlyargs=[], args=[arg(arg='se_lf'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='θ   Ȭɗ    Ȕ   ĩ ˘    \u03a2  ɟÒ̡ ')), If(test=Attribute(value=Name(id='se_lf', ctx=Load()), attr='regressor_columns', ctx=Load()), body=[Assign(targets=[Name(id='exog_future', ctx=Store())], value=Subscript(value=Name(id='df', ctx=Load()), slice=Attribute(value=Name(id='se_lf', ctx=Load()), attr='regressor_columns', ctx=Load()), ctx=Load())), Assign(targets=[Attribute(value=Name(id='exog_future', ctx=Load()), attr='index', ctx=Store())], value=Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='timestamp'), ctx=Load()))], orelse=[Assign(targets=[Name(id='exog_future', ctx=Store())], value=Constant(value=None))]), Return(value=Name(id='exog_future', ctx=Load()))], decorator_list=[], returns=Subscript(value=Name(id='Optional', ctx=Load()), slice=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), ctx=Load())), FunctionDef(name='_make_prediction', args=arguments(posonlyargs=[], args=[arg(arg='se_lf'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), arg(arg='predict', annotation=Name(id='bool', ctx=Load())), arg(arg='quantiles', annotation=Subscript(value=Name(id='Sequence', ctx=Load()), slice=Name(id='float', ctx=Load()), ctx=Load())), arg(arg='dynami', annotation=Name(id='bool', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[If(test=Compare(left=Attribute(value=Name(id='se_lf', ctx=Load()), attr='_fit_results', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='Model is not fitted! Fit the model before calling predict method!')], keywords=[]))], orelse=[]), Assign(targets=[Name(id='HORIZON', ctx=Store())], value=Call(func=Name(id='len', ctx=Load()), args=[Name(id='df', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='se_lf', ctx=Load()), attr='_encode_categoricals', ctx=Load()), args=[Name(id='df', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='se_lf', ctx=Load()), attr='_check_df', ctx=Load()), args=[Name(id='df', ctx=Load()), Name(id='HORIZON', ctx=Load())], keywords=[])), Assign(targets=[Name(id='exog_future', ctx=Store())], value=Call(func=Attribute(value=Name(id='se_lf', ctx=Load()), attr='_select_regressors', ctx=Load()), args=[Name(id='df', ctx=Load())], keywords=[])), Assign(targets=[Name(id='start_timestamp', ctx=Store())], value=Call(func=Attribute(value=Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='timestamp'), ctx=Load()), attr='min', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='end_timestamp', ctx=Store())], value=Call(func=Attribute(value=Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='timestamp'), ctx=Load()), attr='max', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='start_idx', ctx=Store())], value=Call(func=Name(id='determine_num_steps', ctx=Load()), args=[], keywords=[keyword(arg='start_timestamp', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='_first_train_timestamp', ctx=Load())), keyword(arg='end_timestamp', value=Name(id='start_timestamp', ctx=Load())), keyword(arg='freq', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='_freq', ctx=Load()))])), Assign(targets=[Name(id='end_idx', ctx=Store())], value=Call(func=Name(id='determine_num_steps', ctx=Load()), args=[], keywords=[keyword(arg='start_timestamp', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='_first_train_timestamp', ctx=Load())), keyword(arg='end_timestamp', value=Name(id='end_timestamp', ctx=Load())), keyword(arg='freq', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='_freq', ctx=Load()))])), If(test=Name(id='predict', ctx=Load()), body=[Assign(targets=[Tuple(elts=[Name(id='forecast', ctx=Store()), Name(id='_', ctx=Store())], ctx=Store())], value=Call(func=Name(id='seasonal_prediction_with_confidence', ctx=Load()), args=[], keywords=[keyword(arg='arima_res', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='_fit_results', ctx=Load())), keyword(arg='start', value=Name(id='start_idx', ctx=Load())), keyword(arg='end', value=Name(id='end_idx', ctx=Load())), keyword(arg='X', value=Name(id='exog_future', ctx=Load())), keyword(arg='alpha', value=Constant(value=0.05)), keyword(arg='dynamic', value=Name(id='dynami', ctx=Load()))])), Assign(targets=[Name(id='y_pred', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), args=[Dict(keys=[Constant(value='mean')], values=[Name(id='forecast', ctx=Load())])], keywords=[])), For(target=Name(id='quantile', ctx=Store()), iter=Name(id='quantiles', ctx=Load()), body=[Assign(targets=[Name(id='alpha', ctx=Store())], value=Call(func=Name(id='miniii', ctx=Load()), args=[BinOp(left=Name(id='quantile', ctx=Load()), op=Mult(), right=Constant(value=2)), BinOp(left=BinOp(left=Constant(value=1), op=Sub(), right=Name(id='quantile', ctx=Load())), op=Mult(), right=Constant(value=2))], keywords=[])), Assign(targets=[Tuple(elts=[Name(id='_', ctx=Store()), Name(id='borders', ctx=Store())], ctx=Store())], value=Call(func=Name(id='seasonal_prediction_with_confidence', ctx=Load()), args=[], keywords=[keyword(arg='arima_res', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='_fit_results', ctx=Load())), keyword(arg='start', value=Name(id='start_idx', ctx=Load())), keyword(arg='end', value=Name(id='end_idx', ctx=Load())), keyword(arg='X', value=Name(id='exog_future', ctx=Load())), keyword(arg='alpha', value=Name(id='alpha', ctx=Load())), keyword(arg='dynamic', value=Name(id='dynami', ctx=Load()))])), If(test=Compare(left=Name(id='quantile', ctx=Load()), ops=[Lt()], comparators=[BinOp(left=Constant(value=1), op=Div(), right=Constant(value=2))]), body=[Assign(targets=[Name(id='seriesugN', ctx=Store())], value=Subscript(value=Name(id='borders', ctx=Load()), slice=Tuple(elts=[Slice(), Constant(value=0)], ctx=Load()), ctx=Load()))], orelse=[Assign(targets=[Name(id='seriesugN', ctx=Store())], value=Subscript(value=Name(id='borders', ctx=Load()), slice=Tuple(elts=[Slice(), Constant(value=1)], ctx=Load()), ctx=Load()))]), Assign(targets=[Subscript(value=Name(id='y_pred', ctx=Load()), slice=JoinedStr(values=[Constant(value='mean_'), FormattedValue(value=Name(id='quantile', ctx=Load()), conversion=-1, format_spec=JoinedStr(values=[Constant(value='.4g')]))]), ctx=Store())], value=Name(id='seriesugN', ctx=Load()))], orelse=[])], orelse=[Assign(targets=[Tuple(elts=[Name(id='forecast', ctx=Store()), Name(id='_', ctx=Store())], ctx=Store())], value=Call(func=Name(id='seasonal_prediction_with_confidence', ctx=Load()), args=[], keywords=[keyword(arg='arima_res', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='_fit_results', ctx=Load())), keyword(arg='start', value=Name(id='start_idx', ctx=Load())), keyword(arg='end', value=Name(id='end_idx', ctx=Load())), keyword(arg='X', value=Name(id='exog_future', ctx=Load())), keyword(arg='alpha', value=Constant(value=0.05)), keyword(arg='dynamic', value=Name(id='dynami', ctx=Load()))])), Assign(targets=[Name(id='y_pred', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), args=[Dict(keys=[Constant(value='mean')], values=[Name(id='forecast', ctx=Load())])], keywords=[]))]), Assign(targets=[Name(id='rename_dict', ctx=Store())], value=DictComp(key=Name(id='c_olumn', ctx=Load()), value=Call(func=Attribute(value=Name(id='c_olumn', ctx=Load()), attr='replace', ctx=Load()), args=[Constant(value='mean'), Constant(value='target')], keywords=[]), generators=[comprehension(target=Name(id='c_olumn', ctx=Store()), iter=Attribute(value=Name(id='y_pred', ctx=Load()), attr='columns', ctx=Load()), ifs=[Call(func=Attribute(value=Name(id='c_olumn', ctx=Load()), attr='startswith', ctx=Load()), args=[Constant(value='mean')], keywords=[])], is_async=0)])), Assign(targets=[Name(id='y_pred', ctx=Store())], value=Call(func=Attribute(value=Name(id='y_pred', ctx=Load()), attr='rename', ctx=Load()), args=[Name(id='rename_dict', ctx=Load())], keywords=[keyword(arg='axis', value=Constant(value=1))])), Return(value=Name(id='y_pred', ctx=Load()))], decorator_list=[], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), FunctionDef(name='_get_fit', args=arguments(posonlyargs=[], args=[arg(arg='se_lf'), arg(arg='endog', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='Series', ctx=Load())), arg(arg='exog', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='̂ϐ ˸     ț Ň̔   ')), Pass()], decorator_list=[Name(id='abstractmethod', ctx=Load())], returns=Name(id='SARIMAXResultsWrapper', ctx=Load())), FunctionDef(name='get_model', args=arguments(posonlyargs=[], args=[arg(arg='se_lf')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='GetΜ Ƃ˜Ō:pǦƤÆưʽʺy:Ǧclasɑsɓ͑Ϳ»γ:ʎ̋`stǽăaƌPþίǟtsmoEΜ\x80düeŬ΅lΊsƈ.ͯtsa.stǐat͵esƆpace˂.ɏŧǤ´̎sariτmaĶxλN.SqARIMŖAƿȖǢðXRŢ\x9desñýulĮtƝŊsƭWrȈapper` thI\x82ŕĨat̼Ȭ is ěŜʒusxØed inĭsƲiˊde̸ ˜etnaȱ¶ class.\n\nRB3eturnƝļs\n--Þ:-˼--¢-ͻĕǧ˞-\ń:\n   ƒIĝn\x8fĐtƖUϋernaĸl mo\x80ɠ˫de?Ŕl')), Return(value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='_fit_results', ctx=Load()))], decorator_list=[], returns=Name(id='SARIMAXResultsWrapper', ctx=Load())), FunctionDef(name='_check_df', args=arguments(posonlyargs=[], args=[arg(arg='se_lf'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), arg(arg='HORIZON', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='int', ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=None)]), body=[Expr(value=Constant(value='        ϡ ͼ         ')), If(test=Compare(left=Attribute(value=Name(id='se_lf', ctx=Load()), attr='regressor_columns', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='Something went wrong, regressor_columns is None!')], keywords=[]))], orelse=[]), Assign(targets=[Name(id='COLUMN_TO_DROP', ctx=Store())], value=ListComp(elt=Name(id='col', ctx=Load()), generators=[comprehension(target=Name(id='col', ctx=Store()), iter=Attribute(value=Name(id='df', ctx=Load()), attr='columns', ctx=Load()), ifs=[Compare(left=Name(id='col', ctx=Load()), ops=[NotIn()], comparators=[BinOp(left=List(elts=[Constant(value='target'), Constant(value='timestamp')], ctx=Load()), op=Add(), right=Attribute(value=Name(id='se_lf', ctx=Load()), attr='regressor_columns', ctx=Load()))])], is_async=0)])), If(test=Name(id='COLUMN_TO_DROP', ctx=Load()), body=[Expr(value=Call(func=Attribute(value=Name(id='warnings', ctx=Load()), attr='warn', ctx=Load()), args=[], keywords=[keyword(arg='message', value=JoinedStr(values=[Constant(value='SARIMAX model does not work with exogenous features (features unknown in future).\n '), FormattedValue(value=Name(id='COLUMN_TO_DROP', ctx=Load()), conversion=-1), Constant(value=' will be dropped')]))]))], orelse=[]), If(test=Name(id='HORIZON', ctx=Load()), body=[Assign(targets=[Name(id='short_reg', ctx=Store())], value=ListComp(elt=Name(id='_regressor', ctx=Load()), generators=[comprehension(target=Name(id='_regressor', ctx=Store()), iter=Attribute(value=Name(id='se_lf', ctx=Load()), attr='regressor_columns', ctx=Load()), ifs=[Compare(left=Call(func=Attribute(value=Subscript(value=Name(id='df', ctx=Load()), slice=Name(id='_regressor', ctx=Load()), ctx=Load()), attr='count', ctx=Load()), args=[], keywords=[]), ops=[Lt()], comparators=[Name(id='HORIZON', ctx=Load())])], is_async=0)])), If(test=Name(id='short_reg', ctx=Load()), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[JoinedStr(values=[Constant(value='Regressors '), FormattedValue(value=Name(id='short_reg', ctx=Load()), conversion=-1), Constant(value=' are too short for chosen horizon value.\n Try lower horizon value, or drop this regressors.')])], keywords=[]))], orelse=[])], orelse=[])], decorator_list=[]), FunctionDef(name='p', args=arguments(posonlyargs=[], args=[arg(arg='se_lf'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), arg(arg='predict', annotation=Name(id='bool', ctx=Load())), arg(arg='quantiles', annotation=Subscript(value=Name(id='Sequence', ctx=Load()), slice=Name(id='float', ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Co͍Ǥmput̘e țprÈǯeͫȖϘνdictʮ˟ioʬ[ə˱ͪns Ļfrom a xˊS\\ARŸɬI˙MAjX m¢odÞeͥl īand ôȯÈ̻ͥ̋useϠO tǢrŞʁueθ ˰Ǎɟľįiłn-sařm͠ple daǁtʥ\x95a asÊ laΩȸgµsñ iʭÜf əp³ossiŋb˨Ϊle͕.\nŏ˖ư\nȹPar{ametpeŔrϢϠs¤ÂÌ\n-Ɲ--Ȑ--ī--ˈ-·|ƞȭ--\ndĳf:ǆσ\nͻ  ϵȋ  Ő˘Feʵfatuœʁr͗ȉes dǒatafȃǩr̯aƇƩmǎe\npɅredȟ͵iͿǴc͇ϒtiɏonů_inˍterv|a˵(ǎlμ:\n   ĻĀ˜ I\x84ɦ̠f͞ƻ· ϧTrͨue ĕretɼεʚuƮrnsã pr˘əǲed΄i̼ctğΩion inƤɏϪtºervalĒ fΈÅor˽ ̓for̕ecaÇst\n˃qua̓ίntǌͫɠileŹȈs:\nˤ    Levels CoΧfͨģ ͠predŒáictioʡn© diʭŭsǹγtrώibuέ\u03a2tiRon\nàͱʄ\nRe˝͆ƯtuƷrŢnsş\nˎ--ʕɒ̺ϲ--Ć-Ɠ\\-΅-ʔƩ\n:\nìʷ ƽ ϩ  DataϷFrc\xa0laϪɖˎ́EʖmͪÆğǼͫeƐ\x97ť witΡh mpredictʳiĕons')), Return(value=Call(func=Attribute(value=Name(id='se_lf', ctx=Load()), attr='_make_prediction', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='df', ctx=Load())), keyword(arg='prediction_interval', value=Name(id='predict', ctx=Load())), keyword(arg='quantiles', value=Name(id='quantiles', ctx=Load())), keyword(arg='dynamic', value=Constant(value=False))]))], decorator_list=[], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='se_lf')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='regressor_columns', ctx=Store())], value=Constant(value=None)), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='_fit_results', ctx=Store())], value=Constant(value=None)), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='_freq', ctx=Store())], value=Constant(value=None)), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='_first_train_timestamp', ctx=Store())], value=Constant(value=None))], decorator_list=[]), FunctionDef(name='forecast', args=arguments(posonlyargs=[], args=[arg(arg='se_lf'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), arg(arg='predict', annotation=Name(id='bool', ctx=Load())), arg(arg='quantiles', annotation=Subscript(value=Name(id='Sequence', ctx=Load()), slice=Name(id='float', ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=Call(func=Attribute(value=Name(id='se_lf', ctx=Load()), attr='_make_prediction', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='df', ctx=Load())), keyword(arg='prediction_interval', value=Name(id='predict', ctx=Load())), keyword(arg='quantiles', value=Name(id='quantiles', ctx=Load())), keyword(arg='dynamic', value=Constant(value=True))]))], decorator_list=[], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), FunctionDef(name='fit', args=arguments(posonlyargs=[], args=[arg(arg='se_lf'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), arg(arg='regressors', annotation=Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Ʒ(̶Fiͤtsɝ a ¶ɲSARIȊMAX͢ƿ mode¿l.\nɨ\nPʔʹȉaramǉetersʜ\nƳ:-----Ù---ʂ-Ô-\ndˣf:Ȝʨ\nͽ   ʮȝ ŪǙϲFeɳaέtuʠ\x92res d̠ataçfrηame̟ɝ\nrZeǂgˢreěsɋɏţ˯so¨rsɣȜ\x9e͠Ŭ:Γ\nΙ ŜΫř Ł ǆ̺ǺfΗǦ<Ϫ ɏɈList of the cƏoÝlumɆns wi\x9fth regrζes8\x98soˑrŶsϟǆ\nÖȎ\nRetur˻ϑǻns\x86\ǹ-̪------˃\n:\n   v Fittƶed͡ model')), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='regressor_columns', ctx=Store())], value=Name(id='regressors', ctx=Load())), Expr(value=Call(func=Attribute(value=Name(id='se_lf', ctx=Load()), attr='_encode_categoricals', ctx=Load()), args=[Name(id='df', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='se_lf', ctx=Load()), attr='_check_df', ctx=Load()), args=[Name(id='df', ctx=Load())], keywords=[])), Assign(targets=[Name(id='exog_train', ctx=Store())], value=Call(func=Attribute(value=Name(id='se_lf', ctx=Load()), attr='_select_regressors', ctx=Load()), args=[Name(id='df', ctx=Load())], keywords=[])), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='_fit_results', ctx=Store())], value=Call(func=Attribute(value=Name(id='se_lf', ctx=Load()), attr='_get_fit_results', ctx=Load()), args=[], keywords=[keyword(arg='endog', value=Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='target'), ctx=Load())), keyword(arg='exog', value=Name(id='exog_train', ctx=Load()))])), Assign(targets=[Name(id='f_req', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='infer_freq', ctx=Load()), args=[Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='timestamp'), ctx=Load())], keywords=[keyword(arg='warn', value=Constant(value=False))])), If(test=Compare(left=Name(id='f_req', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value="Can't determine frequency of a given dataframe")], keywords=[]))], orelse=[]), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='_freq', ctx=Store())], value=Name(id='f_req', ctx=Load())), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='_first_train_timestamp', ctx=Store())], value=Call(func=Attribute(value=Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='timestamp'), ctx=Load()), attr='min', ctx=Load()), args=[], keywords=[])), Return(value=Name(id='se_lf', ctx=Load()))], decorator_list=[], returns=Constant(value='_SARIMAXBaseAdapter')), FunctionDef(name='_encode_categoricals', args=arguments(posonlyargs=[], args=[arg(arg='se_lf'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='    ̃      Ď         ')), Assign(targets=[Name(id='ca', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Call(func=Attribute(value=Name(id='df', ctx=Load()), attr='select_dtypes', ctx=Load()), args=[], keywords=[keyword(arg='include', value=List(elts=[Constant(value='category')], ctx=Load()))]), attr='columns', ctx=Load()), attr='tolist', ctx=Load()), args=[], keywords=[])), Try(body=[Assign(targets=[Subscript(value=Attribute(value=Name(id='df', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Name(id='ca', ctx=Load())], ctx=Load()), ctx=Store())], value=Call(func=Attribute(value=Subscript(value=Name(id='df', ctx=Load()), slice=Name(id='ca', ctx=Load()), ctx=Load()), attr='astype', ctx=Load()), args=[Name(id='int', ctx=Load())], keywords=[]))], handlers=[ExceptHandler(type=Name(id='ValueError', ctx=Load()), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[JoinedStr(values=[Constant(value='Categorical columns '), FormattedValue(value=Name(id='ca', ctx=Load()), conversion=-1), Constant(value=' can not been converted to int.\n Try to encode this columns manually.')])], keywords=[]))])], orelse=[], finalbody=[])], decorator_list=[], returns=Constant(value=None))], decorator_list=[]), ClassDef(name='_SARIMAXAdapter', bases=[Name(id='_SARIMAXBaseAdapter', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='Ŏ˨Classǎ \x8efƵoîŬrɢ hŜolding ƃSari˦\u0383Ă²Əma\x9fx ͯ\u03a2ȍm3odelɐǊÄ.ɡ\n\nNʆoɃteƳs\n\x9c-ͦ----\nW@ÆeĢ use ɎγSARIM̪AX [1]˃ ņm\x83oděˑel f³rʮom sūκtaǂtk2æsÙmodelsȗ pŮacɲkage. S̥tat̙sYmƫodŐeŠlɅs ʋɏϐpa\x9fckaĔg̢e usesȈ ȗ`e7§xog`Ȑ atçɥtributeιɭʈ f̥Ŷo³ŕϾvït\nųȽ`́exNog¸ÇeϽµϪǋ˱nous ˿reǃΓ\x87greȗʴĨįÎķ͕sĜʬsɇors`ͱ ʟȀ@wh\x95ichȔAͦ shoul¼ɥƟdȼ be ͖kϽnoþwθnĕ iná Σfuʈtur˫e,̭ϲXΣ khowͯ,ɋeΨčvĒerÆϷ weΰń uȋsϐe eϟȂxogenäous for\naȻƕɰd6ditƩiȗĬoǉnìaɘl͛Ǫ feaˣɏΞ͚tŶ\x9b̕uĤrƊʭes» wȬhƉaƥtţƁS ƾi͉s ęnoǏ˓t \x91known Ēiʜ̛dn fuʉ{turɟe,ͫ È˳˯and Äǵreηǋö]ț¶gr͋eˍsǬsƭƣôorsȾ ʱǈΓÌfǴoƧ\u038drƥ featuĉres àweǖ̻ϑ do͉ kƝHnowˌ̍Ϡ̣Ţ\xa0̾ inȯ\nǝfuͥŷtuɧΗÎɮrΝeȱw.\nŐ\n.ˣ. `S˸ARIMAX:̾&ʧ <ʢʠhttpsĶ:͇//ʅww)w˦.ͲstǴΥatDsƔm̾odν˖zeʞlζsa.orAgΈ/ǫstak̂eǚƣbțleȴ́Ä/̇g͵eneŷraȒtļʁΦed/sʙΤ˰tatǫs\xa0ÔƺǣŀmoõϱŃd·els.tsa.staƧʒΚt˨ΆɒeϵsVɿp̒ʽɲ˘aΫc˟Ġeř.sar̵im9rΨaĪx.DSARIMʐAX.htmˬl˥˫>_àņ`')), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='se_lf'), arg(arg='orde', annotation=Subscript(value=Name(id='Tuple', ctx=Load()), slice=Tuple(elts=[Name(id='int', ctx=Load()), Name(id='int', ctx=Load()), Name(id='int', ctx=Load())], ctx=Load()), ctx=Load())), arg(arg='seasonal_order', annotation=Subscript(value=Name(id='Tuple', ctx=Load()), slice=Tuple(elts=[Name(id='int', ctx=Load()), Name(id='int', ctx=Load()), Name(id='int', ctx=Load()), Name(id='int', ctx=Load())], ctx=Load()), ctx=Load())), arg(arg='trend', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load())), arg(arg='measurement_error', annotation=Name(id='bool', ctx=Load())), arg(arg='time_varying_regress', annotation=Name(id='bool', ctx=Load())), arg(arg='mle_regression', annotation=Name(id='bool', ctx=Load())), arg(arg='simple_differencing', annotation=Name(id='bool', ctx=Load())), arg(arg='enforce_stationarit_y', annotation=Name(id='bool', ctx=Load())), arg(arg='enforce_invertibility', annotation=Name(id='bool', ctx=Load())), arg(arg='hamilton', annotation=Name(id='bool', ctx=Load())), arg(arg='concent_rate_scale', annotation=Name(id='bool', ctx=Load())), arg(arg='trend_offsetOl', annotation=Name(id='float', ctx=Load())), arg(arg='use_exact_diffuseUtxY', annotation=Name(id='bool', ctx=Load())), arg(arg='dates', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='datetime', ctx=Load()), ctx=Load()), ctx=Load())), arg(arg='f_req', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load())), arg(arg='missing', annotation=Name(id='str', ctx=Load())), arg(arg='validate_specification', annotation=Name(id='bool', ctx=Load()))], kwonlyargs=[], kw_defaults=[], kwarg=arg(arg='k_wargs'), defaults=[Tuple(elts=[Constant(value=2), Constant(value=1), Constant(value=0)], ctx=Load()), Tuple(elts=[Constant(value=1), Constant(value=1), Constant(value=0), Constant(value=12)], ctx=Load()), Constant(value='c'), Constant(value=False), Constant(value=False), Constant(value=True), Constant(value=False), Constant(value=True), Constant(value=True), Constant(value=False), Constant(value=False), Constant(value=1), Constant(value=False), Constant(value=None), Constant(value=None), Constant(value='none'), Constant(value=True)]), body=[Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='order', ctx=Store())], value=Name(id='orde', ctx=Load())), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='seasonal_order', ctx=Store())], value=Name(id='seasonal_order', ctx=Load())), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='trend', ctx=Store())], value=Name(id='trend', ctx=Load())), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='measurement_error', ctx=Store())], value=Name(id='measurement_error', ctx=Load())), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='time_varying_regression', ctx=Store())], value=Name(id='time_varying_regress', ctx=Load())), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='mle_regression', ctx=Store())], value=Name(id='mle_regression', ctx=Load())), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='simple_differencing', ctx=Store())], value=Name(id='simple_differencing', ctx=Load())), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='enforce_stationarity', ctx=Store())], value=Name(id='enforce_stationarit_y', ctx=Load())), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='enforce_invertibility', ctx=Store())], value=Name(id='enforce_invertibility', ctx=Load())), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='hamilton_representation', ctx=Store())], value=Name(id='hamilton', ctx=Load())), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='concentrate_scale', ctx=Store())], value=Name(id='concent_rate_scale', ctx=Load())), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='trend_offset', ctx=Store())], value=Name(id='trend_offsetOl', ctx=Load())), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='use_exact_diffuse', ctx=Store())], value=Name(id='use_exact_diffuseUtxY', ctx=Load())), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='dates', ctx=Store())], value=Name(id='dates', ctx=Load())), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='freq', ctx=Store())], value=Name(id='f_req', ctx=Load())), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='missing', ctx=Store())], value=Name(id='missing', ctx=Load())), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='validate_specification', ctx=Store())], value=Name(id='validate_specification', ctx=Load())), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='kwargs', ctx=Store())], value=Name(id='k_wargs', ctx=Load())), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[]))], decorator_list=[]), FunctionDef(name='_get_fit', args=arguments(posonlyargs=[], args=[arg(arg='se_lf'), arg(arg='endog', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='Series', ctx=Load())), arg(arg='exog', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='î   ˑ Ǳ   ͋ ɛ   ȴǄ˴')), Assign(targets=[Name(id='endog_np', ctx=Store())], value=Attribute(value=Name(id='endog', ctx=Load()), attr='values', ctx=Load())), Assign(targets=[Name(id='mo', ctx=Store())], value=Call(func=Name(id='SARIMAX', ctx=Load()), args=[], keywords=[keyword(arg='endog', value=Name(id='endog_np', ctx=Load())), keyword(arg='exog', value=Name(id='exog', ctx=Load())), keyword(arg='order', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='order', ctx=Load())), keyword(arg='seasonal_order', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='seasonal_order', ctx=Load())), keyword(arg='trend', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='trend', ctx=Load())), keyword(arg='measurement_error', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='measurement_error', ctx=Load())), keyword(arg='time_varying_regression', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='time_varying_regression', ctx=Load())), keyword(arg='mle_regression', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='mle_regression', ctx=Load())), keyword(arg='simple_differencing', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='simple_differencing', ctx=Load())), keyword(arg='enforce_stationarity', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='enforce_stationarity', ctx=Load())), keyword(arg='enforce_invertibility', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='enforce_invertibility', ctx=Load())), keyword(arg='hamilton_representation', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='hamilton_representation', ctx=Load())), keyword(arg='concentrate_scale', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='concentrate_scale', ctx=Load())), keyword(arg='trend_offset', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='trend_offset', ctx=Load())), keyword(arg='use_exact_diffuse', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='use_exact_diffuse', ctx=Load())), keyword(arg='dates', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='dates', ctx=Load())), keyword(arg='freq', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='freq', ctx=Load())), keyword(arg='missing', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='missing', ctx=Load())), keyword(arg='validate_specification', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='validate_specification', ctx=Load())), keyword(value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='kwargs', ctx=Load()))])), Assign(targets=[Name(id='resultOlF', ctx=Store())], value=Call(func=Attribute(value=Name(id='mo', ctx=Load()), attr='fit', ctx=Load()), args=[], keywords=[])), Return(value=Name(id='resultOlF', ctx=Load()))], decorator_list=[])], decorator_list=[]), ClassDef(name='SARIMAXM_odel', bases=[Name(id='PerSegmentModelMixin', ctx=Load()), Name(id='PredictionIntervalContextIgnorantModelMixin', ctx=Load()), Name(id='PredictionIntervalContextIgnorantAbstractModel', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='ǱCψl?"ϧÆľdÔas̲s for ͨ˫ho̹lĢĉƐdinēg ĨǺSǘarimÙΞúax moΫdιɚelʉ.ɩ\n\nȧMethod ``ɅpeςƀyrAedńict`Ǚǆ` caǳÓn ˧use υtrueΰ tarʠgeëtŻɫ vaǾklΥúes ͱɕƕonly on trƕɣaiʸnąΣ dataNÚÆ ǜoͪnː future Ȓdϲata ɴautoregrͰįȓĂeϧssion\nȨforeÝcastiĒȴn\u038dg wịll̉ͼ be maȹde ˵even ¢iÛfΉ Ƞta¥rgeřtƎţs aĚr\x83e ΐɃϫḱnowΐn.\n\nNȷǦoteūsɴr\n-Ɍ-Κ|---\nWeό usĪϏe :Ʃpy:clũasϳċs:̾Χ`stçaðtsƫ§moɭ®\x8fdŞelsŏ.t0sa.sa̘rŨiķmþax.SřA̎RI˓MAX\x8bî´E\u0382`.$ SɆžtƽϞa˟tʬsÄmoǬx0deh©lsǋ¼ paǰck̶agϐe uʈ̭sesʩ ̻`Ş\x87ex<?ʥoΖæ˭g` aǨ˿6ĠhttŔriϗbușɾt·eŶǍƎ forÂȆ\x9a\n`eɦxogɟƞeͿnou¼s regʕāͭƩe˝r˷essorȎs` úΡwʅhichıÕǲȑ ΓsɵhouldȳƊ´ be knoƝwn iǙn ɀfǤutȿù\x87ǒȗur̋e, ,howeơâ̱vͨʙƦ͌erǨ ̌weǊ ǻxuse͓\x90 eΩxogenœoŋϙusǷɵ forˍʧɾ\n˶adďdŝiΡtþiĩonalŎ featur̤eλs Ɓwha²ĳt ̯ʘ\x95\x9eİis̯\x83 noʉt) knoȽɤΎƕwƪn \x96in fʈu¬Ϗƿture, ˣ˵andȸ ȵǼreęūȟgressUoJrs 9ɘʖʸãěfoȣr ǖfΕeȓʱ͊aÌ\x9f+tureŉs˶ ̃w\x88e ͕doH knʆɤİŷow iɐn˗ɘ\nf!uture.')), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='se_lf'), arg(arg='orde', annotation=Subscript(value=Name(id='Tuple', ctx=Load()), slice=Tuple(elts=[Name(id='int', ctx=Load()), Name(id='int', ctx=Load()), Name(id='int', ctx=Load())], ctx=Load()), ctx=Load())), arg(arg='seasonal_order', annotation=Subscript(value=Name(id='Tuple', ctx=Load()), slice=Tuple(elts=[Name(id='int', ctx=Load()), Name(id='int', ctx=Load()), Name(id='int', ctx=Load()), Name(id='int', ctx=Load())], ctx=Load()), ctx=Load())), arg(arg='trend', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load())), arg(arg='measurement_error', annotation=Name(id='bool', ctx=Load())), arg(arg='time_varying_regress', annotation=Name(id='bool', ctx=Load())), arg(arg='mle_regression', annotation=Name(id='bool', ctx=Load())), arg(arg='simple_differencing', annotation=Name(id='bool', ctx=Load())), arg(arg='enforce_stationarit_y', annotation=Name(id='bool', ctx=Load())), arg(arg='enforce_invertibility', annotation=Name(id='bool', ctx=Load())), arg(arg='hamilton', annotation=Name(id='bool', ctx=Load())), arg(arg='concent_rate_scale', annotation=Name(id='bool', ctx=Load())), arg(arg='trend_offsetOl', annotation=Name(id='float', ctx=Load())), arg(arg='use_exact_diffuseUtxY', annotation=Name(id='bool', ctx=Load())), arg(arg='dates', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='datetime', ctx=Load()), ctx=Load()), ctx=Load())), arg(arg='f_req', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load())), arg(arg='missing', annotation=Name(id='str', ctx=Load())), arg(arg='validate_specification', annotation=Name(id='bool', ctx=Load()))], kwonlyargs=[], kw_defaults=[], kwarg=arg(arg='k_wargs'), defaults=[Tuple(elts=[Constant(value=2), Constant(value=1), Constant(value=0)], ctx=Load()), Tuple(elts=[Constant(value=1), Constant(value=1), Constant(value=0), Constant(value=12)], ctx=Load()), Constant(value='c'), Constant(value=False), Constant(value=False), Constant(value=True), Constant(value=False), Constant(value=True), Constant(value=True), Constant(value=False), Constant(value=False), Constant(value=1), Constant(value=False), Constant(value=None), Constant(value=None), Constant(value='none'), Constant(value=True)]), body=[Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='order', ctx=Store())], value=Name(id='orde', ctx=Load())), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='seasonal_order', ctx=Store())], value=Name(id='seasonal_order', ctx=Load())), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='trend', ctx=Store())], value=Name(id='trend', ctx=Load())), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='measurement_error', ctx=Store())], value=Name(id='measurement_error', ctx=Load())), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='time_varying_regression', ctx=Store())], value=Name(id='time_varying_regress', ctx=Load())), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='mle_regression', ctx=Store())], value=Name(id='mle_regression', ctx=Load())), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='simple_differencing', ctx=Store())], value=Name(id='simple_differencing', ctx=Load())), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='enforce_stationarity', ctx=Store())], value=Name(id='enforce_stationarit_y', ctx=Load())), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='enforce_invertibility', ctx=Store())], value=Name(id='enforce_invertibility', ctx=Load())), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='hamilton_representation', ctx=Store())], value=Name(id='hamilton', ctx=Load())), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='concentrate_scale', ctx=Store())], value=Name(id='concent_rate_scale', ctx=Load())), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='trend_offset', ctx=Store())], value=Name(id='trend_offsetOl', ctx=Load())), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='use_exact_diffuse', ctx=Store())], value=Name(id='use_exact_diffuseUtxY', ctx=Load())), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='dates', ctx=Store())], value=Name(id='dates', ctx=Load())), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='freq', ctx=Store())], value=Name(id='f_req', ctx=Load())), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='missing', ctx=Store())], value=Name(id='missing', ctx=Load())), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='validate_specification', ctx=Store())], value=Name(id='validate_specification', ctx=Load())), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='kwargs', ctx=Store())], value=Name(id='k_wargs', ctx=Load())), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[Name(id='SARIMAXM_odel', ctx=Load()), Name(id='se_lf', ctx=Load())], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[keyword(arg='base_model', value=Call(func=Name(id='_SARIMAXAdapter', ctx=Load()), args=[], keywords=[keyword(arg='order', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='order', ctx=Load())), keyword(arg='seasonal_order', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='seasonal_order', ctx=Load())), keyword(arg='trend', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='trend', ctx=Load())), keyword(arg='measurement_error', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='measurement_error', ctx=Load())), keyword(arg='time_varying_regression', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='time_varying_regression', ctx=Load())), keyword(arg='mle_regression', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='mle_regression', ctx=Load())), keyword(arg='simple_differencing', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='simple_differencing', ctx=Load())), keyword(arg='enforce_stationarity', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='enforce_stationarity', ctx=Load())), keyword(arg='enforce_invertibility', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='enforce_invertibility', ctx=Load())), keyword(arg='hamilton_representation', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='hamilton_representation', ctx=Load())), keyword(arg='concentrate_scale', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='concentrate_scale', ctx=Load())), keyword(arg='trend_offset', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='trend_offset', ctx=Load())), keyword(arg='use_exact_diffuse', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='use_exact_diffuse', ctx=Load())), keyword(arg='dates', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='dates', ctx=Load())), keyword(arg='freq', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='freq', ctx=Load())), keyword(arg='missing', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='missing', ctx=Load())), keyword(arg='validate_specification', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='validate_specification', ctx=Load())), keyword(value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='kwargs', ctx=Load()))]))]))], decorator_list=[])], decorator_list=[])], type_ignores=[])