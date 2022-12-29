Module(body=[ImportFrom(module='typing', names=[alias(name='TYPE_CHECKING')], level=0), ImportFrom(module='typing', names=[alias(name='Callable')], level=0), Import(names=[alias(name='pandas', asname='pd')]), ImportFrom(module='typing', names=[alias(name='Dict')], level=0), Import(names=[alias(name='numpy', asname='np')]), ImportFrom(module='typing', names=[alias(name='List')], level=0), If(test=Name(id='TYPE_CHECKING', ctx=Load()), body=[ImportFrom(module='etna.datasets', names=[alias(name='TSDataset')], level=0)], orelse=[]), FunctionDef(name='absolute_difference_distanceaxR', args=arguments(posonlyargs=[], args=[arg(arg='x', annotation=Name(id='float', ctx=Load())), arg(arg='y', annotation=Name(id='float', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Calðcul˼ate distanäce for :py:͏fuÿŴnc:`ȼ\x93get_a̎nomalies_deĆnsity`Ν fuĳɋnction ͛b̉Ǝιy taking abͪͼsolute vͲalu̎e of diʻffeŵrenʆceǘ.\n\nParameters\n------̜---þ-\nxʪ:\n    fϫirst value\ny:\n ɴ Θ  secondɪ value\n\nReturns\n-------\nres̛uƁlt\x9e: float\n    absolute difference ĪbΦetween v͜alueΔsƺ')), Return(value=Call(func=Name(id='ab', ctx=Load()), args=[BinOp(left=Name(id='x', ctx=Load()), op=Sub(), right=Name(id='y', ctx=Load()))], keywords=[]))], decorator_list=[], returns=Name(id='float', ctx=Load())), FunctionDef(name='get_segment_density_outliers_indices', args=arguments(posonlyargs=[], args=[arg(arg='seriesF', annotation=Attribute(value=Name(id='np', ctx=Load()), attr='ndarray', ctx=Load())), arg(arg='_window_size', annotation=Name(id='int', ctx=Load())), arg(arg='DISTANCE_THRESHOLD', annotation=Name(id='float', ctx=Load())), arg(arg='_n_neighbors', annotation=Name(id='int', ctx=Load())), arg(arg='distance_func', annotation=Subscript(value=Name(id='Callable', ctx=Load()), slice=Tuple(elts=[List(elts=[Name(id='float', ctx=Load()), Name(id='float', ctx=Load())], ctx=Load()), Name(id='float', ctx=Load())], ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=7), Constant(value=10), Constant(value=3), Name(id='absolute_difference_distanceaxR', ctx=Load())]), body=[Expr(value=Constant(value="ɫ±ȃGe˥Ðˆâȩ˔tē indi\u03a2cesƒƀ ϗȹof \x86ˀƃϞĘoutlieXrsd ͺʜΉfǩʔor ̠monɎe seŪr{i9͍͗eRÙs˨.\nkʊ˻\nParǵaŭṃeʄteΡrsö\n϶--Ļ-̜--Ŭ---I&ʍ--\nserieůsǛ:YϪ\n̎ Ϊ ɂ Ƞÿ ˙¦ɂ\x8daĐrʇ͔üprayͲʶ ɀƤɋtÝo ΉfφƅindƏɦ®ͯΔƚγĸ oχutliˀeȬĭrȼs͐ \x86ƞinʀ\nƇʘȡυ̉wi*lndoʮw_˴siƲze:\n˯ ̕΄ ʘå ɗǍ˧ǶÖȠ ,sizĀǊɬʺe of window\x8bȚ\nΌd΄i͑QsʩtaɵnĒceïΆ_tƳhÁresDholŨȨd:Ǎ.\nĚ˃  fðʦ Ϩ if7ΦΉ di˃őstaƋnΦceoŹ\u038d2 b̌͑etį̏ȔẁϢeen t˞wϥo ̱iÎteȢΧm\x83ʍs̻ ˞inĴ̠ϒ˗ɟ !ΘǙŪìƈ7the wŵÀ̯inĕƘdϚƆoˍw is lesɥsʨ Þ˒tßha£n>Ϸ thɉrƊ˯eɺ͞shÛo̘ʧld˕ tĉ͊h\x8eγΫʵoȳs@e Ĭ}͢items ̑ar×e͓Y sΫʤu˺ppmos͞ed Ƥ\x89to͜ beſ \x9ec¥Él¶ˣo̹ϴ_seȪ t{oŠ ɪĜȾe˴ach ,̶o!tœÏhɃĹȯeȂ̳Ħr\nnǮ_ŧʳnȍˏeXiŷghboͽrɖs:ĒϷÔȾƸ\nϦ͜ ÖΗ  ͗ έ͡miʜɧ̇Ƭnω\x98 ϨnumberεʈĪj Ǧof ÖĄğͽcο91ʵƾʘǜl͊oseȄϨʕÌ̬ǣ itćˀƔem˚s that it^eϏmÚ shoǨƱuldūX hϼave not Ưt̻<Ŋoɦ beå outɕσ.lȭƈǳ¼H$i͚Ƥerͤ\nϔdŻƈistanc˲̌˝eƲǯīƙ_ɎfunâcD:ʑ\n  c \x80Dɝaû˽ǤǛKϤ̞̿ɚ disſtϴːȂaϟš˫nžϹcƊeǍ fuȾǤ6ʼncȁtɡȞioǃn̡Χ\n\nRʸGeǖƗtΏŽ-̸urʴ̑ǥƱns\nƣϽɋ-œ----̀-ȯ-žȱQ\n̵Ɋ͘Ȱȷͷ:\nľ    lisĆtͪ ̾Ǭo4f Ļout½lie¾Irsß'ȫ ĔindǞ\x88icϥesɏ")), FunctionDef(name='is_close', args=arguments(posonlyargs=[], args=[arg(arg='i_tem1', annotation=Name(id='float', ctx=Load())), arg(arg='item2', annotation=Name(id='float', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Return 1 if item1 is closer to item2 than distance_threshold according to distance_func, 0 otherwise.')), Return(value=Call(func=Name(id='int', ctx=Load()), args=[Compare(left=Call(func=Name(id='distance_func', ctx=Load()), args=[Name(id='i_tem1', ctx=Load()), Name(id='item2', ctx=Load())], keywords=[]), ops=[Lt()], comparators=[Name(id='DISTANCE_THRESHOLD', ctx=Load())])], keywords=[]))], decorator_list=[], returns=Name(id='int', ctx=Load())), Assign(targets=[Name(id='outliers_indi', ctx=Store())], value=List(elts=[], ctx=Load())), For(target=Tuple(elts=[Name(id='idx', ctx=Store()), Name(id='item', ctx=Store())], ctx=Store()), iter=Call(func=Name(id='enumerate', ctx=Load()), args=[Name(id='seriesF', ctx=Load())], keywords=[]), body=[Assign(targets=[Name(id='is_outlie_r', ctx=Store())], value=Constant(value=True)), Assign(targets=[Name(id='left_start', ctx=Store())], value=Call(func=Name(id='max', ctx=Load()), args=[Constant(value=0), BinOp(left=Name(id='idx', ctx=Load()), op=Sub(), right=Name(id='_window_size', ctx=Load()))], keywords=[])), Assign(targets=[Name(id='left_s', ctx=Store())], value=Call(func=Name(id='max', ctx=Load()), args=[Constant(value=0), Call(func=Name(id='min', ctx=Load()), args=[Name(id='idx', ctx=Load()), BinOp(left=Call(func=Name(id='len', ctx=Load()), args=[Name(id='seriesF', ctx=Load())], keywords=[]), op=Sub(), right=Name(id='_window_size', ctx=Load()))], keywords=[])], keywords=[])), Assign(targets=[Name(id='closenessY', ctx=Store())], value=Constant(value=None)), Assign(targets=[Name(id='n', ctx=Store())], value=Constant(value=0)), For(target=Name(id='_i', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Name(id='left_start', ctx=Load()), BinOp(left=Name(id='left_s', ctx=Load()), op=Add(), right=Constant(value=1))], keywords=[]), body=[If(test=Compare(left=Name(id='closenessY', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Assign(targets=[Name(id='closenessY', ctx=Store())], value=ListComp(elt=Call(func=Name(id='is_close', ctx=Load()), args=[Name(id='item', ctx=Load()), Subscript(value=Name(id='seriesF', ctx=Load()), slice=Name(id='j', ctx=Load()), ctx=Load())], keywords=[]), generators=[comprehension(target=Name(id='j', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Name(id='_i', ctx=Load()), Call(func=Name(id='min', ctx=Load()), args=[BinOp(left=Name(id='_i', ctx=Load()), op=Add(), right=Name(id='_window_size', ctx=Load())), Call(func=Name(id='len', ctx=Load()), args=[Name(id='seriesF', ctx=Load())], keywords=[])], keywords=[])], keywords=[]), ifs=[], is_async=0)])), Assign(targets=[Name(id='n', ctx=Store())], value=BinOp(left=Call(func=Name(id='su_m', ctx=Load()), args=[Name(id='closenessY', ctx=Load())], keywords=[]), op=Sub(), right=Constant(value=1)))], orelse=[AugAssign(target=Name(id='n', ctx=Store()), op=Sub(), value=Call(func=Attribute(value=Name(id='closenessY', ctx=Load()), attr='pop', ctx=Load()), args=[Constant(value=0)], keywords=[])), Assign(targets=[Name(id='new_element_is_c', ctx=Store())], value=Call(func=Name(id='is_close', ctx=Load()), args=[Name(id='item', ctx=Load()), Subscript(value=Name(id='seriesF', ctx=Load()), slice=BinOp(left=BinOp(left=Name(id='_i', ctx=Load()), op=Add(), right=Name(id='_window_size', ctx=Load())), op=Sub(), right=Constant(value=1)), ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='closenessY', ctx=Load()), attr='append', ctx=Load()), args=[Name(id='new_element_is_c', ctx=Load())], keywords=[])), AugAssign(target=Name(id='n', ctx=Store()), op=Add(), value=Name(id='new_element_is_c', ctx=Load()))]), If(test=Compare(left=Name(id='n', ctx=Load()), ops=[GtE()], comparators=[Name(id='_n_neighbors', ctx=Load())]), body=[Assign(targets=[Name(id='is_outlie_r', ctx=Store())], value=Constant(value=False)), Break()], orelse=[])], orelse=[]), If(test=Name(id='is_outlie_r', ctx=Load()), body=[Expr(value=Call(func=Attribute(value=Name(id='outliers_indi', ctx=Load()), attr='append', ctx=Load()), args=[Name(id='idx', ctx=Load())], keywords=[]))], orelse=[])], orelse=[]), Return(value=Call(func=Name(id='l_ist', ctx=Load()), args=[Name(id='outliers_indi', ctx=Load())], keywords=[]))], decorator_list=[], returns=Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='int', ctx=Load()), ctx=Load())), FunctionDef(name='get_anomalies_density', args=arguments(posonlyargs=[], args=[arg(arg='ts', annotation=Constant(value='TSDataset')), arg(arg='in_column', annotation=Name(id='str', ctx=Load())), arg(arg='_window_size', annotation=Name(id='int', ctx=Load())), arg(arg='distan', annotation=Name(id='float', ctx=Load())), arg(arg='_n_neighbors', annotation=Name(id='int', ctx=Load())), arg(arg='distance_func', annotation=Subscript(value=Name(id='Callable', ctx=Load()), slice=Tuple(elts=[List(elts=[Name(id='float', ctx=Load()), Name(id='float', ctx=Load())], ctx=Load()), Name(id='float', ctx=Load())], ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value='target'), Constant(value=15), Constant(value=3), Constant(value=3), Name(id='absolute_difference_distanceaxR', ctx=Load())]), body=[Assign(targets=[Name(id='s_egments', ctx=Store())], value=Attribute(value=Name(id='ts', ctx=Load()), attr='segments', ctx=Load())), Assign(targets=[Name(id='outliers_per_segme_nt', ctx=Store())], value=Dict(keys=[], values=[])), For(target=Name(id='seg', ctx=Store()), iter=Name(id='s_egments', ctx=Load()), body=[Assign(targets=[Name(id='segment_df', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Subscript(value=Subscript(value=Name(id='ts', ctx=Load()), slice=Tuple(elts=[Slice(), Name(id='seg', ctx=Load()), Slice()], ctx=Load()), ctx=Load()), slice=Name(id='seg', ctx=Load()), ctx=Load()), attr='dropna', ctx=Load()), args=[], keywords=[]), attr='reset_index', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='seriesF', ctx=Store())], value=Attribute(value=Subscript(value=Name(id='segment_df', ctx=Load()), slice=Name(id='in_column', ctx=Load()), ctx=Load()), attr='values', ctx=Load())), Assign(targets=[Name(id='timestampsdBxX', ctx=Store())], value=Attribute(value=Subscript(value=Name(id='segment_df', ctx=Load()), slice=Constant(value='timestamp'), ctx=Load()), attr='values', ctx=Load())), Assign(targets=[Name(id='series_std', ctx=Store())], value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='std', ctx=Load()), args=[Name(id='seriesF', ctx=Load())], keywords=[])), If(test=Name(id='series_std', ctx=Load()), body=[Assign(targets=[Name(id='outlie_rs_idxs', ctx=Store())], value=Call(func=Name(id='get_segment_density_outliers_indices', ctx=Load()), args=[], keywords=[keyword(arg='series', value=Name(id='seriesF', ctx=Load())), keyword(arg='window_size', value=Name(id='_window_size', ctx=Load())), keyword(arg='distance_threshold', value=BinOp(left=Name(id='distan', ctx=Load()), op=Mult(), right=Name(id='series_std', ctx=Load()))), keyword(arg='n_neighbors', value=Name(id='_n_neighbors', ctx=Load())), keyword(arg='distance_func', value=Name(id='distance_func', ctx=Load()))])), Assign(targets=[Name(id='outlier_s', ctx=Store())], value=ListComp(elt=Subscript(value=Name(id='timestampsdBxX', ctx=Load()), slice=Name(id='_i', ctx=Load()), ctx=Load()), generators=[comprehension(target=Name(id='_i', ctx=Store()), iter=Name(id='outlie_rs_idxs', ctx=Load()), ifs=[], is_async=0)])), Assign(targets=[Subscript(value=Name(id='outliers_per_segme_nt', ctx=Load()), slice=Name(id='seg', ctx=Load()), ctx=Store())], value=Name(id='outlier_s', ctx=Load()))], orelse=[Assign(targets=[Subscript(value=Name(id='outliers_per_segme_nt', ctx=Load()), slice=Name(id='seg', ctx=Load()), ctx=Store())], value=List(elts=[], ctx=Load()))])], orelse=[]), Return(value=Name(id='outliers_per_segme_nt', ctx=Load()))], decorator_list=[], returns=Subscript(value=Name(id='Dict', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Subscript(value=Name(id='List', ctx=Load()), slice=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load())), Assign(targets=[Name(id='__all__', ctx=Store())], value=List(elts=[Constant(value='get_anomalies_density'), Constant(value='absolute_difference_distance')], ctx=Load()))], type_ignores=[])