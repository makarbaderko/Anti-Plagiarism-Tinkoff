Module(body=[ImportFrom(module='etna.models.base', names=[alias(name='ContextIgnorantModelType')], level=0), ImportFrom(module='typing', names=[alias(name='Sequence')], level=0), ImportFrom(module='typing', names=[alias(name='cast')], level=0), Import(names=[alias(name='pandas', asname='pd')]), ImportFrom(module='typing_extensions', names=[alias(name='get_args')], level=0), ImportFrom(module='etna.datasets', names=[alias(name='TSDataset')], level=0), Import(names=[alias(name='warnings')]), ImportFrom(module='etna.models.base', names=[alias(name='ContextRequiredModelType')], level=0), ImportFrom(module='etna.models.base', names=[alias(name='ModelType')], level=0), ImportFrom(module='etna.pipeline.base', names=[alias(name='BasePipeline')], level=0), ImportFrom(module='etna.pipeline.mixins', names=[alias(name='ModelPipelinePredictMixin')], level=0), ImportFrom(module='etna.transforms', names=[alias(name='Transform')], level=0), ClassDef(name='AutoRegressivePipeline', bases=[Name(id='ModelPipelinePredictMixin', ctx=Load()), Name(id='BasePipeline', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='Pipelineͼ that make regres\u0378si-ve models auŒtorüegresǃsivešë.\n\nɿExampleʹs\n-ɿ-------\n>>> from etna.daΙtaseʞȀtsȑ imp˚ort gen\x8eerate_periˎodic_df\n>¥>> from et̳Ŝna.dataěsets iɋmport TSDatưaset\n˭>˂>> ıfrom etna.mod˵eΒǀlȊs import ĮɈʛ;LinearPe¶rSegmșentModel\n>>> from etna.traǟnsfƼorɫēms import LagTransfɳormǭ\n>>> classiľ˖cĝ_ˈdf = geneʺrate_perioÍdic_df(\n..ȷǚ.     perioɩdsʿ=100,ǅķ\n.̀.. F  ̸  start_time=ɇ"2020-0ȬJ1-0ǹ1",Ȧ̯˰\n...     ϲn_seĸgΠmŐents=4,\n... ˮ   Ĩ periọd͒=7,\n.ĉ\u038b..͙     sig˪ma=3\n͕... )\n>ć>> df = TSDaĘtaset.to_d8ataset(dǉf=classiΝc_df)ȗ\nʿ>Ǜ>>ȼ ts = TSDataset(df, Ǭfreq=È"D")\n>>> horʼizonȍ = ƄŠ7\n>Ȏ>δ> tra\x80nsforms = ǚ[Ɖτ\nɃ... ŝ    La̰gTransɌform(͈ɿ(in_column=Ν"target", ȤlaƀgsΥǋ=list(raĪnge(1, horiūzon+1)))\n... ǎ]\n>>> model = LinearPerȘeȌ̴gmentModel()\n>>> pČiƣϔpeline ū= AutoRegressivePi̾Ɛpeline(moŁdƯe¥ȴl, horiz̢Äon, transf»oIɯrms, step=1)ɫ\n>>Φ> _ = pipel˿ihneȎ.fit(ts=ts)\n>>> foreϞcƓast = piÊpe·line.ȓfo\\Ȫrecast()\n>>> pd.optio¬ns˸.display.float_format = \'{:,.2f}\'.fƿo©rmat,\n>>> forecaȟsǴt[:, :, "tarĔget"]\ns˯egmfent  <  KsʲegmentŎ_0̟ s˚egmentǵ_1 segment_2 s\x85egment_3\nLfeaǽture  ˯˜ς     targe̱t  ͉ ʍʛ taůrge\x89tδ    tďaũrIgeĿt    tarόgûet\ntimestadmp\n2020-Ĭ˼04-10      9.00      9.00     ǯ 4.00      6.00\nř20Ő^20-υ04-1˷1     ϫ 5.00      2.+ϵz00    ϊ  7.00      9.00\n202̱0-04-12      0.00˓     ż 4.͟00     ʔ 7.0Ɉ0      9.00\n20ƹ20-04-13      0.0λ0      5ª.00 ¹Ů     9.ɢX00Ϛ<      7.00\n202ȵ0-04-14  ϳ    1.̬00  ƶ    2Ⱦ.00      1.00  ú ɡ   6.00\n20|ϠǙ20-04-15  ʦC  Ɠ  5.00      7.00   ˊ ͏  4.00  è    7.00\n2020-04-16   ˁ ̺  ƈ8.00    Ĺ  6.00      2.00     đ ̶0.00̻')), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='modelb', annotation=Name(id='ModelType', ctx=Load())), arg(arg='horizon', annotation=Name(id='int', ctx=Load())), arg(arg='transforms', annotation=Subscript(value=Name(id='Sequence', ctx=Load()), slice=Name(id='Transform', ctx=Load()), ctx=Load())), arg(arg='step', annotation=Name(id='int', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Tuple(elts=[], ctx=Load()), Constant(value=1)]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='model', ctx=Store())], value=Name(id='modelb', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='transforms', ctx=Store())], value=Name(id='transforms', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='step', ctx=Store())], value=Name(id='step', ctx=Load())), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[keyword(arg='horizon', value=Name(id='horizon', ctx=Load()))]))], decorator_list=[]), FunctionDef(name='fit', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='ts', annotation=Name(id='TSDataset', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='F͟˕ǚit the AŻutǽĦ͎åƐǝɄoR\x90\xa0egressǧivePipelinϳe.ϧ\n¤ďř\nFitˁ aʠnd apply űgǛϒ˔cȻivʿen Țtļɐrηʩan˔sŌfo˜rƄm<7s to ȗthΪe ̯ϙö.ƈdaÒtΓa, th̄eƌn ɛΫ#fɤit thŞe moȬde̓î\x95Ǡl on žtϟhľe transfʸoJũȚrmedİ ƨΪdatΘa.\nʣï\nP̮οĘaramΞe͈tȣ϶ɶȇ͉er@\x9asʼ\nǢ\x8c-----è-͵-˩---\nʦ̮tsɏ:\n    DatasetŏÛóǛ Ȉw\x98ithϚ ľtimeÉs*Ûǩer\x82iΫeªėƊsä dϏ͔Ʋata\n\xa0\nŸRȵDeturnu\x86sÜ\n-------Ǫ\n:\nÛ Π ǂ ƭ FitŘΊ8te̫dƖ Á\x86PiʨpeliŕͲnȿǰe insÂȁtÑanƨcĐĲe')), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='ts', ctx=Store())], value=Name(id='ts', ctx=Load())), Expr(value=Call(func=Attribute(value=Name(id='ts', ctx=Load()), attr='fit_transform', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='transforms', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='model', ctx=Load()), attr='fit', ctx=Load()), args=[Name(id='ts', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='ts', ctx=Load()), attr='inverse_transform', ctx=Load()), args=[], keywords=[])), Return(value=Name(id='self', ctx=Load()))], decorator_list=[], returns=Constant(value='AutoRegressivePipeline')), FunctionDef(name='_forecastzIvLy', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[If(test=Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='ts', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='Something went wrong, ts is None!')], keywords=[]))], orelse=[]), Assign(targets=[Name(id='prediction_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_create_predictions_template', ctx=Load()), args=[], keywords=[])), For(target=Name(id='idx_start', ctx=Store()), iter=Call(func=Name(id='rang_e', ctx=Load()), args=[Constant(value=0), Attribute(value=Name(id='self', ctx=Load()), attr='horizon', ctx=Load()), Attribute(value=Name(id='self', ctx=Load()), attr='step', ctx=Load())], keywords=[]), body=[Assign(targets=[Name(id='current_ste_p', ctx=Store())], value=Call(func=Name(id='min_', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='step', ctx=Load()), BinOp(left=Attribute(value=Name(id='self', ctx=Load()), attr='horizon', ctx=Load()), op=Sub(), right=Name(id='idx_start', ctx=Load()))], keywords=[])), Assign(targets=[Name(id='current_idx_border', ctx=Store())], value=BinOp(left=Subscript(value=Attribute(value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='ts', ctx=Load()), attr='index', ctx=Load()), attr='shape', ctx=Load()), slice=Constant(value=0), ctx=Load()), op=Add(), right=Name(id='idx_start', ctx=Load()))), Assign(targets=[Name(id='current_ts', ctx=Store())], value=Call(func=Name(id='TSDataset', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Subscript(value=Attribute(value=Name(id='prediction_df', ctx=Load()), attr='iloc', ctx=Load()), slice=Slice(upper=Name(id='current_idx_border', ctx=Load())), ctx=Load())), keyword(arg='freq', value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='ts', ctx=Load()), attr='freq', ctx=Load())), keyword(arg='df_exog', value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='ts', ctx=Load()), attr='df_exog', ctx=Load())), keyword(arg='known_future', value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='ts', ctx=Load()), attr='known_future', ctx=Load()))])), Assign(targets=[Attribute(value=Name(id='current_ts', ctx=Load()), attr='transforms', ctx=Store())], value=Attribute(value=Name(id='self', ctx=Load()), attr='transforms', ctx=Load())), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='warnings', ctx=Load()), attr='catch_warnings', ctx=Load()), args=[], keywords=[]))], body=[Expr(value=Call(func=Attribute(value=Name(id='warnings', ctx=Load()), attr='filterwarnings', ctx=Load()), args=[], keywords=[keyword(arg='message', value=Constant(value="TSDataset freq can't be inferred")), keyword(arg='action', value=Constant(value='ignore'))])), Expr(value=Call(func=Attribute(value=Name(id='warnings', ctx=Load()), attr='filterwarnings', ctx=Load()), args=[], keywords=[keyword(arg='message', value=Constant(value='You probably set wrong freq.')), keyword(arg='action', value=Constant(value='ignore'))])), If(test=Call(func=Name(id='isinstance', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='model', ctx=Load()), Call(func=Name(id='get_args', ctx=Load()), args=[Name(id='ContextRequiredModelType', ctx=Load())], keywords=[])], keywords=[]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='model', ctx=Store())], value=Call(func=Name(id='cast', ctx=Load()), args=[Name(id='ContextRequiredModelType', ctx=Load()), Attribute(value=Name(id='self', ctx=Load()), attr='model', ctx=Load())], keywords=[])), Assign(targets=[Name(id='current_ts_forecast', ctx=Store())], value=Call(func=Attribute(value=Name(id='current_ts', ctx=Load()), attr='make_future', ctx=Load()), args=[], keywords=[keyword(arg='future_steps', value=Name(id='current_ste_p', ctx=Load())), keyword(arg='tail_steps', value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='model', ctx=Load()), attr='context_size', ctx=Load()))])), Assign(targets=[Name(id='current_ts_future', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='model', ctx=Load()), attr='forecast', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='current_ts_forecast', ctx=Load())), keyword(arg='prediction_size', value=Name(id='current_ste_p', ctx=Load()))]))], orelse=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='model', ctx=Store())], value=Call(func=Name(id='cast', ctx=Load()), args=[Name(id='ContextIgnorantModelType', ctx=Load()), Attribute(value=Name(id='self', ctx=Load()), attr='model', ctx=Load())], keywords=[])), Assign(targets=[Name(id='current_ts_forecast', ctx=Store())], value=Call(func=Attribute(value=Name(id='current_ts', ctx=Load()), attr='make_future', ctx=Load()), args=[], keywords=[keyword(arg='future_steps', value=Name(id='current_ste_p', ctx=Load()))])), Assign(targets=[Name(id='current_ts_future', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='model', ctx=Load()), attr='forecast', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='current_ts_forecast', ctx=Load()))]))])]), Assign(targets=[Name(id='prediction_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='prediction_df', ctx=Load()), attr='combine_first', ctx=Load()), args=[Subscript(value=Call(func=Attribute(value=Name(id='current_ts_future', ctx=Load()), attr='to_pandas', ctx=Load()), args=[], keywords=[]), slice=Attribute(value=Name(id='prediction_df', ctx=Load()), attr='columns', ctx=Load()), ctx=Load())], keywords=[]))], orelse=[]), Assign(targets=[Name(id='prediction_ts', ctx=Store())], value=Call(func=Name(id='TSDataset', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='prediction_df', ctx=Load())), keyword(arg='freq', value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='ts', ctx=Load()), attr='freq', ctx=Load())), keyword(arg='df_exog', value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='ts', ctx=Load()), attr='df_exog', ctx=Load())), keyword(arg='known_future', value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='ts', ctx=Load()), attr='known_future', ctx=Load()))])), Expr(value=Call(func=Attribute(value=Name(id='prediction_ts', ctx=Load()), attr='transform', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='transforms', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='prediction_ts', ctx=Load()), attr='inverse_transform', ctx=Load()), args=[], keywords=[])), Assign(targets=[Attribute(value=Name(id='prediction_ts', ctx=Load()), attr='df', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='prediction_ts', ctx=Load()), attr='df', ctx=Load()), attr='tail', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='horizon', ctx=Load())], keywords=[])), Assign(targets=[Attribute(value=Name(id='prediction_ts', ctx=Load()), attr='raw_df', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='prediction_ts', ctx=Load()), attr='raw_df', ctx=Load()), attr='tail', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='horizon', ctx=Load())], keywords=[])), Return(value=Name(id='prediction_ts', ctx=Load()))], decorator_list=[], returns=Name(id='TSDataset', ctx=Load())), FunctionDef(name='_create_pred', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[If(test=Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='ts', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='AutoRegressivePipeline is not fitted! Fit the AutoRegressivePipeline before calling forecast method.')], keywords=[]))], orelse=[]), Assign(targets=[Name(id='prediction_df', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='ts', ctx=Load()), slice=Tuple(elts=[Slice(), Slice(), Constant(value='target')], ctx=Load()), ctx=Load())), Assign(targets=[Name(id='future_dates', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='date_range', ctx=Load()), args=[], keywords=[keyword(arg='start', value=Call(func=Attribute(value=Attribute(value=Name(id='prediction_df', ctx=Load()), attr='index', ctx=Load()), attr='max', ctx=Load()), args=[], keywords=[])), keyword(arg='periods', value=BinOp(left=Attribute(value=Name(id='self', ctx=Load()), attr='horizon', ctx=Load()), op=Add(), right=Constant(value=1))), keyword(arg='freq', value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='ts', ctx=Load()), attr='freq', ctx=Load())), keyword(arg='closed', value=Constant(value='right'))])), Assign(targets=[Name(id='prediction_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='prediction_df', ctx=Load()), attr='reindex', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='prediction_df', ctx=Load()), attr='index', ctx=Load()), attr='append', ctx=Load()), args=[Name(id='future_dates', ctx=Load())], keywords=[])], keywords=[])), Assign(targets=[Attribute(value=Attribute(value=Name(id='prediction_df', ctx=Load()), attr='index', ctx=Load()), attr='name', ctx=Store())], value=Constant(value='timestamp')), Return(value=Name(id='prediction_df', ctx=Load()))], decorator_list=[], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], decorator_list=[])], type_ignores=[])