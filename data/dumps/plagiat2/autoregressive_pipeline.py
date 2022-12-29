Module(body=[Import(names=[alias(name='warnings')]), ImportFrom(module='typing', names=[alias(name='Sequence')], level=0), ImportFrom(module='etna.pipeline.base', names=[alias(name='BasePipeline')], level=0), Import(names=[alias(name='pandas', asname='pd')]), ImportFrom(module='typing_extensions', names=[alias(name='get_args')], level=0), ImportFrom(module='etna.models.base', names=[alias(name='ContextIgnorantModelType')], level=0), ImportFrom(module='etna.models.base', names=[alias(name='ModelType')], level=0), ImportFrom(module='etna.models.base', names=[alias(name='ContextRequiredModelType')], level=0), ImportFrom(module='etna.datasets', names=[alias(name='TSDataset')], level=0), ImportFrom(module='typing', names=[alias(name='cast')], level=0), ImportFrom(module='etna.pipeline.mixins', names=[alias(name='ModelPipelinePredictMixin')], level=0), ImportFrom(module='etna.transforms', names=[alias(name='Transform')], level=0), ClassDef(name='AutoRegressivePipeline', bases=[Name(id='ModelPipelinePredictMixin', ctx=Load()), Name(id='BasePipeline', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='ĮPŋi§peline that mʹa͌kɳ©e rüʚe1gʈresȅǖ\x88ȤsiɱƍǨvɁȚ\x8eƈϼ˻ʄe mǙ×odEels̭ȽƬ autŚorζŽϱeŤgresĜsiv£ʉ̺ˈe.Σ\nǺ\nƗƏEÜxamŃplesŒÝ\nș--ŏ---Ǎ̳˧̙-óɒ-ɔ\u0378ə-ĩ\nuʤ>̒Ϫ>>Ɖ frćoθȝmǉ Ňȗ͜etϣna.da¬nȎ˭ĸtasπets͎ƹ ɸƫŤ˥ʚim͑pʹorȥʞtYå geƯ̈̌nerͲaɬt͎Σe_ɈŚΟpeǩriʺo²d·ic˕_dʊɳ|fǥǁ\n>Ɣ>Α>ɘΖǷʼͪ ÊfΙr¨š͢ƮŗoȩǙm getna̝̤.ÅdaΪtȎēasȇΗŠtŠʰs imɦÅƥp̂orĠt ̖TʘSDΗ\u0379aȾt\x8a̡aɉseƸt\nȤ>>Ľ>ʄϩßãȋ fƂϑrom eĬtǿ˞ˑnaƀ.Ĺmɗ|1ΧoJdδ͐¼elsçǧ̭Ȅʰ îǣəmƔporǏɭtĨ LiĽ\x92nʯȢdΑe̪ƾȯabrȓėPeƓrοS˱egͪme̬nεˮĥtMŝodeʡ\x9bl\nv>>ϧÜ>Ć ȜĿɨfȁrom etnaδļ\x9fǞ.ƏʴίtȘr\x89Εůęansf©ĪϭormÙ̫˄Ŕs\x97 ǹ\u0383impo̤͖řrÅpǚt LƂaϤɧȣǧĠϦʺgTrϮanμɛsfoǎrm\n>>Ŋ2> ʑǼclaͬDϹss\u0381iɉ4c͍_ʦdĭf =ϋU ǏāgʐeɍͩȒ͚«nerɩ˓aȳteƗȜ_p\x95e&ri˧od̅ic\x8f_?2Ύdf(\nŃȾ...̯ ˰ ĶğÐɝǗϿ ϓ  peɒrio,ŢΐdJst=10¹0,\n.ϓδ͕..Ú˘ A ˟  ȭŃ ɭsÃĭtartΨèŭ_tϗimɴe\x9a="2Ǻ0$20-͍͡č01ɟ-0\\1ąȅ°÷",ͮɇ\nû.ʚ.. ϭ  ɿΐ  nŬ́_űsĚeκgmƽents=4,\nɳ...ƀʝ     ĘŨă®p¶ʕÄ˓ȴe̡§rioĠdĚ=7ˇϣ,ˍ̺Þ\n.!..\x9bɻ¸ń  ̈́   sigmɷ̰͉̯a=3\x9f\năƗ... )\n̻>>> dʌΌϨ͘f ŧ^Ζ= ˟T́ʫɤΜSΈDatasͪet.to_daƽtase̵t(dŌfͺ=cḷ\x87Ƈaʆ°Ǝsřs¢ic΅_dˆf)\n>>ɣϯ̟˳>ù tşήâɺʓĽƆsȡ ̊=͋ TSDya͎tưưaČØɽset(ȡdf°, ˥ɹ\x99]΅fƋͦr΅eǵqĪ=Ɣ"ώέϷȻD̍˶"Υ)`!\nĂʙXÑ>>>Ί ̽ϸhˬo̹rĠ\u0382ɽǋΠ~izonλ ƻɠΞƑ=ǽ ȿȃ7\nʀ>ί>>Ʋ trɤϙaŇͩ͵ɠnôϕsfoϮ±rˑ\x9bǊȣmsțï ſɎ=ȴĵ [̎\nʚʙŞ..\x9b.   Ŵ ʘ LagϺ͑\x94̦ĻɫĢT͓rans²form(δviɩƪ/ǑÍĀǿn_ɽco̊lummnϠ=»"t4ùa»ŻǼrgĪeƧΜt", ΊƩ¶lačgsȀ=listξ(ranƗgeɇ(1ʗ̼&ό,˜ horǇ˪izoȿnǑ+\x9f1ˤɡ)ȼà)εΛ˟ȡÀ)~\n... ]\n>>̻ƙ> mζźodˣe\x89l\x88 φ= L8̼inǊeȼaȂr͗oP\x9dŘĩerθSʩǾΉegĉʠmeƻntĹMoµɻϩε\x90dɶĤieĀl(ł)\nȰ>^>Ŏ>Ǉ pipeĤl̬iʲn̊ǃdĴe Ϲ= ζAutoɷRĒegressϚƐiʬvePipe¨lƹEiĢnśe(Ͽ/˲moǉdφϢeŹΠlŁȓ˱,ŕ»Ř h\x7fʍoȤriʃzĦoʤn9À, Ɏtraʹśnsform͗Ţ͐ϯ\x86sȃȿ, ʠsʞtepVȃĮƅǉϓ=1˻)\n>>ǭϤ>Ǎ¤ Ȁ_ê\x91 = ɦpiνŞpeī͞Ɵli̫ǞneȜʂ.͓fεM̓ÔΰiɆϒt(͋ƣçŠ˴tƊs=ts)\n>>%ÿǵ> ƯÐfďo$Ǘr«ǴeǅcasȁȊϿɰŞͤt˦ =̘ pʺi\'peȃ\x8eʬlŵin\x9deƐ.foreκc̮Ǣ%Ͼ̺a\u038dst(Κ)ʨ\n>ΐ>>p Δǅpdɗ\x8b.optɄĪɏͳionsƪ˾ω.ƦdiʨʝspĪăϞloayʮϜ.floϢĖaƫĉhªtʡǍ_\x8b)ˡfȎȝψ̯͛ùƈϛǊoʑr)mʘatνė =Ɲɒ̡̏Û ϏƲ\x98\'{:,.ȫ˂˜2f}\'.fόΆ͡įorɒm\u0383aˋƯt\nˣ\x9c̩̭˻ƥ>>>ʶϽ foreΔ¤ȓcasĭt[8Ø:,ȣ :, "targeĶtĔȢ"]\n˯ṡegÏͺmentɉ̆   Ω sƬeʱ\x8a¨gmeˬnt_0ŷ s´eĄ̜ȔτÅƠgme\'XÔ̭nt»Îdϵ_1 sőegmǎûent_2 űǱsegȃm;τeʮďnʬt_3\nfǏeatĂOureǟ.˽      ʽɫƳ\x98 Ƣ-Ǐtar̊ʃÂKɼȯg͌͐϶®ʰʏɼƁφet    ƓtaûrΉget ǂ  ŗ tΪaǹrget    t͝ȄaŸrgeƃʉ̛Ͷt\n\x82ź̑ti˓meʵstampȣΥ\n2H0̊ȫ2¬09Ď-0ō4-1ǣή˰0  ˻    9.þ0Ά0ɛ ȯ Ç ͔ ! ʊ ɼ9.Δέ\u038b0Ď͚0  !  εʶ  Ɨ4?ȠɘǊ.ɣ00      6̳ϰ.Rŋy00ŕǍʽʉ\nȮ20ʱȔ)œ2α0Ǖ̗ϩ¼Ł-̏Ʋȝ0š4_ʊʩ-Κ11ţ    ί Έ͏ Ô˼͂5ɡ.¾0̨0ȚĐʱ\x8fβΔ  ɉ  ϺŶAô  Œ2.00 ̞d  Ƀ  ŉ\x8c 7.Ⱥ0ͽ0 ˝ΛȠõˣ  U \x84 Ȟ 9.̆µ0Α\u03780Ɔʓ\n~20̝2qò(0ē_Ù-Ǖ0ʵ÷˕;4ŲΌ-ͭ12  ɣɻ   ŬǇ 0.0ǒ0Α Ξ˫  ɮ   4.\x7f00ʴP  ȉåȕ  ʑɠɃ ̵ Ƕ˵7.xĐ"ˆ²Ǡ¥00ħ2 Ūϡ   ƛ  ˬ9.ʱ͖ɲ0ȝη0\n2\x8b02̴0Ͽ-04-1ȠΨ.˝ȏʪ3 Ŋ̫ ʏ ̥Τ  S² 0.00åϾ  ǒ ϭé  ͦ 5.0̀0£ʊ    ʨϽ  9˼Đ.Ĺ0Ϝ0 Ż  \x83ȃ̯ ΪŰ \u0383 7.0ʺ̵Ǒ0ȳ̫;ǚζƃßĢ:\nŴ2020-04-͚ɘȉ1Ϲȿ4ʢ     ϲͳώ 1.đ0ϖĎ0ĺϬ\x84  ̸̍ώĕ˰ Ɍ   Ʈɿĳǅ2̧.ˎτ00ɝ  ˅ţƒ[ƻ ÿ  ÙϧɈŨȊ WŔʓƇ1͑.0λ0   ̆ė   ďŐʟȈ6ġ.0ƒ&ȟ0ŊɥϮō\nǹŝΛ20ſ20Ε-ėʘ04ÿ˅-Ϗ15̕ȿΕ  ˱ o  Ƣ£ 5ȥ˱.00  º ŉ ̳\x95̣ ı 7τ.v00   êϡ3  ʟŃ ǠЀ»4.V00ʄ Ė ̕ ɠ  : 7¢(.ʀ00\n2Ä020-¼0Κ4˦-ǩ1Ʒ(6ǀ  Σȶʥ  ̀  ψ8ɒ.00  ʍ  ̪ͨʁʚɓɊȔɸ yϗ̐ 6.ͤ0F0 Ǎ × ̐ ƫ ĺ ˿ΗΑ2.Ǣ00Ιʽ  Π̥    0.0˂0͔')), FunctionDef(name='_forecastXmE', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='ƕMake˫ pr¢edic̞tťions.')), If(test=Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='ts', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Raise(exc=Call(func=Name(id='valueerror', ctx=Load()), args=[Constant(value='Something went wrong, ts is None!')], keywords=[]))], orelse=[]), Assign(targets=[Name(id='prediction_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_create_predictions_template', ctx=Load()), args=[], keywords=[])), For(target=Name(id='idx_start', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Constant(value=0), Attribute(value=Name(id='self', ctx=Load()), attr='horizon', ctx=Load()), Attribute(value=Name(id='self', ctx=Load()), attr='step', ctx=Load())], keywords=[]), body=[Assign(targets=[Name(id='current_step', ctx=Store())], value=Call(func=Name(id='min', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='step', ctx=Load()), BinOp(left=Attribute(value=Name(id='self', ctx=Load()), attr='horizon', ctx=Load()), op=Sub(), right=Name(id='idx_start', ctx=Load()))], keywords=[])), Assign(targets=[Name(id='current_idx_border', ctx=Store())], value=BinOp(left=Subscript(value=Attribute(value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='ts', ctx=Load()), attr='index', ctx=Load()), attr='shape', ctx=Load()), slice=Constant(value=0), ctx=Load()), op=Add(), right=Name(id='idx_start', ctx=Load()))), Assign(targets=[Name(id='curren_t_ts', ctx=Store())], value=Call(func=Name(id='TSDataset', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Subscript(value=Attribute(value=Name(id='prediction_df', ctx=Load()), attr='iloc', ctx=Load()), slice=Slice(upper=Name(id='current_idx_border', ctx=Load())), ctx=Load())), keyword(arg='freq', value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='ts', ctx=Load()), attr='freq', ctx=Load())), keyword(arg='df_exog', value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='ts', ctx=Load()), attr='df_exog', ctx=Load())), keyword(arg='known_future', value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='ts', ctx=Load()), attr='known_future', ctx=Load()))])), Assign(targets=[Attribute(value=Name(id='curren_t_ts', ctx=Load()), attr='transforms', ctx=Store())], value=Attribute(value=Name(id='self', ctx=Load()), attr='transforms', ctx=Load())), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='warnings', ctx=Load()), attr='catch_warnings', ctx=Load()), args=[], keywords=[]))], body=[Expr(value=Call(func=Attribute(value=Name(id='warnings', ctx=Load()), attr='filterwarnings', ctx=Load()), args=[], keywords=[keyword(arg='message', value=Constant(value="TSDataset freq can't be inferred")), keyword(arg='action', value=Constant(value='ignore'))])), Expr(value=Call(func=Attribute(value=Name(id='warnings', ctx=Load()), attr='filterwarnings', ctx=Load()), args=[], keywords=[keyword(arg='message', value=Constant(value='You probably set wrong freq.')), keyword(arg='action', value=Constant(value='ignore'))])), If(test=Call(func=Name(id='isinstance', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='model', ctx=Load()), Call(func=Name(id='get_args', ctx=Load()), args=[Name(id='ContextRequiredModelType', ctx=Load())], keywords=[])], keywords=[]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='model', ctx=Store())], value=Call(func=Name(id='cast', ctx=Load()), args=[Name(id='ContextRequiredModelType', ctx=Load()), Attribute(value=Name(id='self', ctx=Load()), attr='model', ctx=Load())], keywords=[])), Assign(targets=[Name(id='current_ts_forecast', ctx=Store())], value=Call(func=Attribute(value=Name(id='curren_t_ts', ctx=Load()), attr='make_future', ctx=Load()), args=[], keywords=[keyword(arg='future_steps', value=Name(id='current_step', ctx=Load())), keyword(arg='tail_steps', value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='model', ctx=Load()), attr='context_size', ctx=Load()))])), Assign(targets=[Name(id='current_ts_future', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='model', ctx=Load()), attr='forecast', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='current_ts_forecast', ctx=Load())), keyword(arg='prediction_size', value=Name(id='current_step', ctx=Load()))]))], orelse=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='model', ctx=Store())], value=Call(func=Name(id='cast', ctx=Load()), args=[Name(id='ContextIgnorantModelType', ctx=Load()), Attribute(value=Name(id='self', ctx=Load()), attr='model', ctx=Load())], keywords=[])), Assign(targets=[Name(id='current_ts_forecast', ctx=Store())], value=Call(func=Attribute(value=Name(id='curren_t_ts', ctx=Load()), attr='make_future', ctx=Load()), args=[], keywords=[keyword(arg='future_steps', value=Name(id='current_step', ctx=Load()))])), Assign(targets=[Name(id='current_ts_future', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='model', ctx=Load()), attr='forecast', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='current_ts_forecast', ctx=Load()))]))])]), Assign(targets=[Name(id='prediction_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='prediction_df', ctx=Load()), attr='combine_first', ctx=Load()), args=[Subscript(value=Call(func=Attribute(value=Name(id='current_ts_future', ctx=Load()), attr='to_pandas', ctx=Load()), args=[], keywords=[]), slice=Attribute(value=Name(id='prediction_df', ctx=Load()), attr='columns', ctx=Load()), ctx=Load())], keywords=[]))], orelse=[]), Assign(targets=[Name(id='prediction_', ctx=Store())], value=Call(func=Name(id='TSDataset', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='prediction_df', ctx=Load())), keyword(arg='freq', value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='ts', ctx=Load()), attr='freq', ctx=Load())), keyword(arg='df_exog', value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='ts', ctx=Load()), attr='df_exog', ctx=Load())), keyword(arg='known_future', value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='ts', ctx=Load()), attr='known_future', ctx=Load()))])), Expr(value=Call(func=Attribute(value=Name(id='prediction_', ctx=Load()), attr='transform', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='transforms', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='prediction_', ctx=Load()), attr='inverse_transform', ctx=Load()), args=[], keywords=[])), Assign(targets=[Attribute(value=Name(id='prediction_', ctx=Load()), attr='df', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='prediction_', ctx=Load()), attr='df', ctx=Load()), attr='tail', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='horizon', ctx=Load())], keywords=[])), Assign(targets=[Attribute(value=Name(id='prediction_', ctx=Load()), attr='raw_df', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='prediction_', ctx=Load()), attr='raw_df', ctx=Load()), attr='tail', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='horizon', ctx=Load())], keywords=[])), Return(value=Name(id='prediction_', ctx=Load()))], decorator_list=[], returns=Name(id='TSDataset', ctx=Load())), FunctionDef(name='fi', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='t', annotation=Name(id='TSDataset', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Fit the AutoRegressivePipeline.̿\n\nFit and apply given tärɎansforms to the data, thʍen fit the model on the transfoťrmed data.\n\nParameterşs\n----------\nts:\n    Dataset with timeseries data\n\nReturns\n-------\n:\n    Fitted Pipeline instance')), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='ts', ctx=Store())], value=Name(id='t', ctx=Load())), Expr(value=Call(func=Attribute(value=Name(id='t', ctx=Load()), attr='fit_transform', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='transforms', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='model', ctx=Load()), attr='fit', ctx=Load()), args=[Name(id='t', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='ts', ctx=Load()), attr='inverse_transform', ctx=Load()), args=[], keywords=[])), Return(value=Name(id='self', ctx=Load()))], decorator_list=[], returns=Constant(value='AutoRegressivePipeline')), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='model', annotation=Name(id='ModelType', ctx=Load())), arg(arg='horizon', annotation=Name(id='intTv', ctx=Load())), arg(arg='transforms', annotation=Subscript(value=Name(id='Sequence', ctx=Load()), slice=Name(id='Transform', ctx=Load()), ctx=Load())), arg(arg='step', annotation=Name(id='intTv', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Tuple(elts=[], ctx=Load()), Constant(value=1)]), body=[Expr(value=Constant(value='Create instance˻ o\u038dͷf ʓƨAuʓtoRegressivePipeli϶nÈe\u0379\x93 witαh Ɵgi˒veŵnˎ parameteŸ̎rs.\n\nPa\x80Ȁramʽeters\n---------ʩ-λ\n¶modIǱel:\n   ʸ I«Ɣȭnst͊ǻa˲nc̄eͨ oˆf the etna ǫ̢Model\njhoriΞzƆƶoʡn:b\n    ɥNumbΚer ɽof˨ time,stʉa̝mps in the futɓure foš˭rC ͫforťeơcaˤst΅in\x8fVg\ntˊrÜansfÃΪϵȁormǗɍΆs˕:\n î Ǖ  Sequence of theʇȢ tŶǳrHanŬēsforms\nstep:\n ϯ   Size Ϛoνfč γpreέdictͰion f©Ɩor ̠Ùonehìk stΒepĩϏ ϙof\x83Ď ͯfoͭrecasting,')), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='model', ctx=Store())], value=Name(id='model', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='transforms', ctx=Store())], value=Name(id='transforms', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='step', ctx=Store())], value=Name(id='step', ctx=Load())), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[keyword(arg='horizon', value=Name(id='horizon', ctx=Load()))]))], decorator_list=[]), FunctionDef(name='_create_predictions_template', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[If(test=Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='ts', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Raise(exc=Call(func=Name(id='valueerror', ctx=Load()), args=[Constant(value='AutoRegressivePipeline is not fitted! Fit the AutoRegressivePipeline before calling forecast method.')], keywords=[]))], orelse=[]), Assign(targets=[Name(id='prediction_df', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='ts', ctx=Load()), slice=Tuple(elts=[Slice(), Slice(), Constant(value='target')], ctx=Load()), ctx=Load())), Assign(targets=[Name(id='future_dates', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='date_range', ctx=Load()), args=[], keywords=[keyword(arg='start', value=Call(func=Attribute(value=Attribute(value=Name(id='prediction_df', ctx=Load()), attr='index', ctx=Load()), attr='max', ctx=Load()), args=[], keywords=[])), keyword(arg='periods', value=BinOp(left=Attribute(value=Name(id='self', ctx=Load()), attr='horizon', ctx=Load()), op=Add(), right=Constant(value=1))), keyword(arg='freq', value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='ts', ctx=Load()), attr='freq', ctx=Load())), keyword(arg='closed', value=Constant(value='right'))])), Assign(targets=[Name(id='prediction_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='prediction_df', ctx=Load()), attr='reindex', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='prediction_df', ctx=Load()), attr='index', ctx=Load()), attr='append', ctx=Load()), args=[Name(id='future_dates', ctx=Load())], keywords=[])], keywords=[])), Assign(targets=[Attribute(value=Attribute(value=Name(id='prediction_df', ctx=Load()), attr='index', ctx=Load()), attr='name', ctx=Store())], value=Constant(value='timestamp')), Return(value=Name(id='prediction_df', ctx=Load()))], decorator_list=[], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], decorator_list=[])], type_ignores=[])