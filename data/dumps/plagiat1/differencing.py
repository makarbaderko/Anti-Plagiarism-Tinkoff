Module(body=[ImportFrom(module='typing', names=[alias(name='Dict')], level=0), ImportFrom(module='typing', names=[alias(name='List')], level=0), ImportFrom(module='typing', names=[alias(name='Optional')], level=0), ImportFrom(module='typing', names=[alias(name='Set')], level=0), ImportFrom(module='typing', names=[alias(name='Union')], level=0), Import(names=[alias(name='numpy', asname='np')]), Import(names=[alias(name='pandas', asname='pd')]), ImportFrom(module='etna.transforms.base', names=[alias(name='Transform')], level=0), ImportFrom(module='etna.transforms.utils', names=[alias(name='match_target_quantiles')], level=0), ClassDef(name='_SingleDifferencingTransform', bases=[Name(id='Transform', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='C̅a͔ȫlciulːateɍd ǩa jtime serįies diȭfferen`cΡȓe\x9eǂƼs of orTde±r 1ĩ˵.\n\nTɈhisǒ ;tɎraɼnsform caɰn worßǻ§ĝΠkŷ wdȋth ̓Na˾Ns \x81at thne begϧinnihͯng o̮f7Ȓ˿ĉ the segme,nt, ͼƍbutǸ Ėfails pwhŬȳeƓnǃ meíʭets NaN in<side ēthe\x90 sȩegmentɂ.\n\nŢNotϝȺesη\n-Ⱦ--Ą--\nTo undeƞrstɚand how trĹanusfoɍrm wȩǽ³ϔƒorkŻs weű recoϪmmeZnd:\nō`Statʌimʷon˱arity aͯnd Dićfferenci˝Ȟng <httpƻs\x9a://otexϾts.ĠcomǇŐ/fpąp2/st͛aɥtionariűtΓy.html>ű`˟_')), FunctionDef(name='_reconstruct_test', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), arg(arg='columns_to_inverse', annotation=Subscript(value=Name(id='Set', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='RŚąʋłͷecoɕnstǴϞrȬuctũ thƶe σçͥteδst in `Ϥì`inͫv˒e°ʕĀǄ/ϯʔÖ¶rέseƶ̞_traͯns΅foñ͉rm``.̼')), Assign(targets=[Name(id='SEGMENTS', ctx=Store())], value=Call(func=Name(id='sorted', ctx=Load()), args=[Call(func=Name(id='SET', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='df', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='segment')], keywords=[])], keywords=[])], keywords=[])), Assign(targets=[Name(id='result_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='df', ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='expected_min_test_timestamp', ctx=Store())], value=Subscript(value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='date_range', ctx=Load()), args=[], keywords=[keyword(arg='start', value=Call(func=Attribute(value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_test_init_df', ctx=Load()), attr='index', ctx=Load()), attr='max', ctx=Load()), args=[], keywords=[])), keyword(arg='periods', value=Constant(value=2)), keyword(arg='freq', value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='infer_freq', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='_train_timestamp', ctx=Load())], keywords=[])), keyword(arg='closed', value=Constant(value='right'))]), slice=Constant(value=0), ctx=Load())), If(test=Compare(left=Name(id='expected_min_test_timestamp', ctx=Load()), ops=[NotEq()], comparators=[Call(func=Attribute(value=Attribute(value=Name(id='df', ctx=Load()), attr='index', ctx=Load()), attr='min', ctx=Load()), args=[], keywords=[])]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='Test should go after the train without gaps')], keywords=[]))], orelse=[]), For(target=Name(id='column_', ctx=Store()), iter=Name(id='columns_to_inverse', ctx=Load()), body=[Assign(targets=[Name(id='to_transform', ctx=Store())], value=Call(func=Attribute(value=Subscript(value=Attribute(value=Name(id='df', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Name(id='SEGMENTS', ctx=Load()), Name(id='column_', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='init_df', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_test_init_df', ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='init_df', ctx=Load()), attr='columns', ctx=Load()), attr='set_levels', ctx=Load()), args=[List(elts=[Name(id='column_', ctx=Load())], ctx=Load())], keywords=[keyword(arg='level', value=Constant(value='feature')), keyword(arg='inplace', value=Constant(value=True))])), Assign(targets=[Name(id='to_transform', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='concat', ctx=Load()), args=[List(elts=[Name(id='init_df', ctx=Load()), Name(id='to_transform', ctx=Load())], ctx=Load())], keywords=[])), If(test=Compare(left=Call(func=Attribute(value=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='to_transform', ctx=Load()), attr='isna', ctx=Load()), args=[], keywords=[]), attr='sum', ctx=Load()), args=[], keywords=[]), attr='sum', ctx=Load()), args=[], keywords=[]), ops=[Gt()], comparators=[Constant(value=0)]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[JoinedStr(values=[Constant(value='There should be no NaNs inside the segments')])], keywords=[]))], orelse=[]), Assign(targets=[Name(id='to_transform', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_make_inv_diff', ctx=Load()), args=[Name(id='to_transform', ctx=Load())], keywords=[])), Assign(targets=[Subscript(value=Attribute(value=Name(id='result_df', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Name(id='SEGMENTS', ctx=Load()), Name(id='column_', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Store())], value=Name(id='to_transform', ctx=Load()))], orelse=[]), Return(value=Name(id='result_df', ctx=Load()))], decorator_list=[], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), FunctionDef(name='_get_column_name', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[If(test=Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='out_column', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Return(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='__repr__', ctx=Load()), args=[], keywords=[]))], orelse=[Return(value=Attribute(value=Name(id='self', ctx=Load()), attr='out_column', ctx=Load()))])], decorator_list=[], returns=Name(id='str', ctx=Load())), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='in_column', annotation=Name(id='str', ctx=Load())), arg(arg='period', annotation=Name(id='int', ctx=Load())), arg(arg='inplace', annotation=Name(id='bool', ctx=Load())), arg(arg='out_column', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=1), Constant(value=True), Constant(value=None)]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Store())], value=Name(id='in_column', ctx=Load())), If(test=BoolOp(op=Or(), values=[UnaryOp(op=Not(), operand=Call(func=Name(id='isinstance', ctx=Load()), args=[Name(id='period', ctx=Load()), Name(id='int', ctx=Load())], keywords=[])), Compare(left=Name(id='period', ctx=Load()), ops=[Lt()], comparators=[Constant(value=1)])]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='Period should be at least 1')], keywords=[]))], orelse=[]), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='period', ctx=Store())], value=Name(id='period', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='inplace', ctx=Store())], value=Name(id='inplace', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='out_column', ctx=Store())], value=Name(id='out_column', ctx=Load())), AnnAssign(target=Attribute(value=Name(id='self', ctx=Load()), attr='_train_timestamp', ctx=Store()), annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Attribute(value=Name(id='pd', ctx=Load()), attr='DatetimeIndex', ctx=Load()), ctx=Load()), value=Constant(value=None), simple=0), AnnAssign(target=Attribute(value=Name(id='self', ctx=Load()), attr='_train_init_dict', ctx=Store()), annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Subscript(value=Name(id='Dict', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Attribute(value=Name(id='pd', ctx=Load()), attr='Series', ctx=Load())], ctx=Load()), ctx=Load()), ctx=Load()), value=Constant(value=None), simple=0), AnnAssign(target=Attribute(value=Name(id='self', ctx=Load()), attr='_test_init_df', ctx=Store()), annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), ctx=Load()), value=Constant(value=None), simple=0)], decorator_list=[]), FunctionDef(name='_make_inv_diff', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='to_transform', annotation=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), Attribute(value=Name(id='pd', ctx=Load()), attr='Series', ctx=Load())], ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[For(target=Name(id='i', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='period', ctx=Load())], keywords=[]), body=[Assign(targets=[Subscript(value=Attribute(value=Name(id='to_transform', ctx=Load()), attr='iloc', ctx=Load()), slice=Slice(lower=Name(id='i', ctx=Load()), step=Attribute(value=Name(id='self', ctx=Load()), attr='period', ctx=Load())), ctx=Store())], value=Call(func=Attribute(value=Subscript(value=Attribute(value=Name(id='to_transform', ctx=Load()), attr='iloc', ctx=Load()), slice=Slice(lower=Name(id='i', ctx=Load()), step=Attribute(value=Name(id='self', ctx=Load()), attr='period', ctx=Load())), ctx=Load()), attr='cumsum', ctx=Load()), args=[], keywords=[]))], orelse=[]), Return(value=Name(id='to_transform', ctx=Load()))], decorator_list=[], returns=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), Attribute(value=Name(id='pd', ctx=Load()), attr='Series', ctx=Load())], ctx=Load()), ctx=Load())), FunctionDef(name='transform', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Make ύa¦ ȨdiŬfĔfeÇˍren;ˍ˷cinǓȏgƆ traʚnƷˡʶAͬͤsfoŋrƹmationō.\n\nPˊ;ĬaraÊmeEteƬärɞùìs\n---͂ťm-nş----ǐ˳--\ndfĿ:Ɖ\n   Đ ɖ˂da˄ʊ˚ȍtafĭ̻rame w˒ith datȘɖaPƷ to9Δ tÖrɪansǠf̏Ƅorm.\x94̃ʽ\n¬͆ϒŶŔ\nRe͌tΫʾu\x8bærns\n--ǯ̝-ʹ-Ɠ-V͞½-ĪʽˏǪŀ-\nresĤuʢlt:¤̤͞% ɉĀpd.ʯ̝DatΙǌafra̹Όmeǌ\n ̸ ϔ  tƜran0sfÏÃƫormX\u0380Ǭeɾdȯ dŝɯ½ƎτaĔ˩Ʒ§taf1ʃrͪaοme')), If(test=BoolOp(op=Or(), values=[Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='_train_init_dict', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='_test_init_df', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='_train_timestamp', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)])]), body=[Raise(exc=Call(func=Name(id='AttributeError', ctx=Load()), args=[Constant(value='Transform is not fitted')], keywords=[]))], orelse=[]), Assign(targets=[Name(id='SEGMENTS', ctx=Store())], value=Call(func=Name(id='sorted', ctx=Load()), args=[Call(func=Name(id='SET', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='df', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='segment')], keywords=[])], keywords=[])], keywords=[])), Assign(targets=[Name(id='transformed', ctx=Store())], value=Call(func=Attribute(value=Subscript(value=Attribute(value=Name(id='df', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Name(id='SEGMENTS', ctx=Load()), Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[])), For(target=Name(id='current_segment', ctx=Store()), iter=Name(id='SEGMENTS', ctx=Load()), body=[Assign(targets=[Name(id='to_transform', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='transformed', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Name(id='current_segment', ctx=Load()), Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load())), Assign(targets=[Name(id='start_idx', ctx=Store())], value=Call(func=Attribute(value=Name(id='to_transform', ctx=Load()), attr='first_valid_index', ctx=Load()), args=[], keywords=[])), Assign(targets=[Subscript(value=Attribute(value=Name(id='transformed', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(lower=Name(id='start_idx', ctx=Load())), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Name(id='current_segment', ctx=Load()), Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Store())], value=Call(func=Attribute(value=Subscript(value=Attribute(value=Name(id='to_transform', ctx=Load()), attr='loc', ctx=Load()), slice=Slice(lower=Name(id='start_idx', ctx=Load())), ctx=Load()), attr='diff', ctx=Load()), args=[], keywords=[keyword(arg='periods', value=Attribute(value=Name(id='self', ctx=Load()), attr='period', ctx=Load()))]))], orelse=[]), If(test=Attribute(value=Name(id='self', ctx=Load()), attr='inplace', ctx=Load()), body=[Assign(targets=[Name(id='result_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='df', ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[])), Assign(targets=[Subscript(value=Attribute(value=Name(id='result_df', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Name(id='SEGMENTS', ctx=Load()), Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Store())], value=Name(id='transformed', ctx=Load()))], orelse=[Assign(targets=[Name(id='transformed_features', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), args=[Name(id='transformed', ctx=Load())], keywords=[keyword(arg='columns', value=Attribute(value=Subscript(value=Attribute(value=Name(id='df', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Name(id='SEGMENTS', ctx=Load()), Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load()), attr='columns', ctx=Load())), keyword(arg='index', value=Attribute(value=Name(id='df', ctx=Load()), attr='index', ctx=Load()))])), Assign(targets=[Name(id='column_nameSXqC', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_get_column_name', ctx=Load()), args=[], keywords=[])), Assign(targets=[Attribute(value=Name(id='transformed_features', ctx=Load()), attr='columns', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='pd', ctx=Load()), attr='MultiIndex', ctx=Load()), attr='from_product', ctx=Load()), args=[List(elts=[Name(id='SEGMENTS', ctx=Load()), List(elts=[Name(id='column_nameSXqC', ctx=Load())], ctx=Load())], ctx=Load())], keywords=[])), Assign(targets=[Name(id='result_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='concat', ctx=Load()), args=[Tuple(elts=[Name(id='df', ctx=Load()), Name(id='transformed_features', ctx=Load())], ctx=Load())], keywords=[keyword(arg='axis', value=Constant(value=1))])), Assign(targets=[Name(id='result_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='result_df', ctx=Load()), attr='sort_index', ctx=Load()), args=[], keywords=[keyword(arg='axis', value=Constant(value=1))]))]), Return(value=Name(id='result_df', ctx=Load()))], decorator_list=[], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), FunctionDef(name='inverse_transform', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Apply invØersãe tŸr§ƯKanɗsfoϬrmϐ4ϯatioƳĈƻn ̻tˆoÎ ΟDatǴaFɊĬrame.ÿ\n\nP\xa0ɎarƵameteƨrsëϏ\n---Ʋ-Ȩƹ--%-ɞ-ʒ˶-˛-\nd¢ƒf:˚\n ɓ   DaˁtŇaFìraȼme tEo appl\x98y invƛeǀƐrse tranʕsЀfȲorm.\n\nÏ¹cRetu͒rns\n---Ķ---ʦ-\nresuˮlt: pʉΣ̐d.DamtǨaFr°ame\x94pµ\n̪ ˊ ͐Ʃ  trƛanżsfŻo̽rˤmÝed ΄DǮataˈFr\x93ameȨ.')), If(test=BoolOp(op=Or(), values=[Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='_train_init_dict', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='_test_init_df', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='_train_timestamp', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)])]), body=[Raise(exc=Call(func=Name(id='AttributeError', ctx=Load()), args=[Constant(value='Transform is not fitted')], keywords=[]))], orelse=[]), If(test=UnaryOp(op=Not(), operand=Attribute(value=Name(id='self', ctx=Load()), attr='inplace', ctx=Load())), body=[Return(value=Name(id='df', ctx=Load()))], orelse=[]), Assign(targets=[Name(id='columns_to_inverse', ctx=Store())], value=Set(elts=[Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load())])), If(test=Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load()), ops=[Eq()], comparators=[Constant(value='target')]), body=[Expr(value=Call(func=Attribute(value=Name(id='columns_to_inverse', ctx=Load()), attr='update', ctx=Load()), args=[Call(func=Name(id='match_target_quantiles', ctx=Load()), args=[Call(func=Name(id='SET', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='df', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='feature')], keywords=[])], keywords=[])], keywords=[])], keywords=[]))], orelse=[]), If(test=BoolOp(op=And(), values=[Compare(left=Subscript(value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_train_timestamp', ctx=Load()), attr='shape', ctx=Load()), slice=Constant(value=0), ctx=Load()), ops=[Eq()], comparators=[Subscript(value=Attribute(value=Attribute(value=Name(id='df', ctx=Load()), attr='index', ctx=Load()), attr='shape', ctx=Load()), slice=Constant(value=0), ctx=Load())]), Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='all', ctx=Load()), args=[Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='_train_timestamp', ctx=Load()), ops=[Eq()], comparators=[Attribute(value=Name(id='df', ctx=Load()), attr='index', ctx=Load())])], keywords=[])]), body=[Assign(targets=[Name(id='result_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_reconstruct_train', ctx=Load()), args=[Name(id='df', ctx=Load()), Name(id='columns_to_inverse', ctx=Load())], keywords=[]))], orelse=[If(test=Compare(left=Call(func=Attribute(value=Attribute(value=Name(id='df', ctx=Load()), attr='index', ctx=Load()), attr='min', ctx=Load()), args=[], keywords=[]), ops=[Gt()], comparators=[Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_train_timestamp', ctx=Load()), attr='max', ctx=Load()), args=[], keywords=[])]), body=[Assign(targets=[Name(id='result_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_reconstruct_test', ctx=Load()), args=[Name(id='df', ctx=Load()), Name(id='columns_to_inverse', ctx=Load())], keywords=[]))], orelse=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='Inverse transform can be applied only to full train or test that should be in the future')], keywords=[]))])]), Return(value=Name(id='result_df', ctx=Load()))], decorator_list=[], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), FunctionDef(name='_reconstruct_train', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), arg(arg='columns_to_inverse', annotation=Subscript(value=Name(id='Set', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='SEGMENTS', ctx=Store())], value=Call(func=Name(id='sorted', ctx=Load()), args=[Call(func=Name(id='SET', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='df', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='segment')], keywords=[])], keywords=[])], keywords=[])), Assign(targets=[Name(id='result_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='df', ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[])), For(target=Name(id='current_segment', ctx=Store()), iter=Name(id='SEGMENTS', ctx=Load()), body=[Assign(targets=[Name(id='init_segment', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_train_init_dict', ctx=Load()), slice=Name(id='current_segment', ctx=Load()), ctx=Load())), For(target=Name(id='column_', ctx=Store()), iter=Name(id='columns_to_inverse', ctx=Load()), body=[Assign(targets=[Name(id='cur_series', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='result_df', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Name(id='current_segment', ctx=Load()), Name(id='column_', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load())), Assign(targets=[Subscript(value=Name(id='cur_series', ctx=Load()), slice=Attribute(value=Name(id='init_segment', ctx=Load()), attr='index', ctx=Load()), ctx=Store())], value=Attribute(value=Name(id='init_segment', ctx=Load()), attr='values', ctx=Load())), Assign(targets=[Name(id='cur_series', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_make_inv_diff', ctx=Load()), args=[Name(id='cur_series', ctx=Load())], keywords=[])), Assign(targets=[Subscript(value=Attribute(value=Name(id='result_df', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Attribute(value=Name(id='cur_series', ctx=Load()), attr='index', ctx=Load()), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Name(id='current_segment', ctx=Load()), Name(id='column_', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Store())], value=Name(id='cur_series', ctx=Load()))], orelse=[])], orelse=[]), Return(value=Name(id='result_df', ctx=Load()))], decorator_list=[], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), FunctionDef(name='fitCk', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='ĀFit̎ ǟtɞƝ͊ʬˆįh˹ʑe »trΝa̒nsľ˶ǶΗXform.\n\nPɺʠaramΟe_teɩr˓ΑʾΩs\n--{-ʄ-Ĝ---X-ȶďĠ·¢-ųǲ-ƴɎÝɊ\nƧdf:\n ͡  ʻ ΚʎdataƸfĄramĵΉϳe ˆwͣȁʅith dǘaŘˣ͔ǳ\x85wta.\n\nReturŗnĪŚͯsðț\n--7-®-\x8c-ťϹȵ--òǯ\nrÿ͍es/ġ=uʹ̕lýtƃ:ɳ Uτċ_BSing̒ǹlųeŃDiϖUffereInõciênƤ˼gǦɮTransfN̘´ϗɧorÚmǮΓ͝ĥōϮ')), Assign(targets=[Name(id='SEGMENTS', ctx=Store())], value=Call(func=Name(id='sorted', ctx=Load()), args=[Call(func=Name(id='SET', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='df', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='segment')], keywords=[])], keywords=[])], keywords=[])), Assign(targets=[Name(id='fit_df', ctx=Store())], value=Call(func=Attribute(value=Subscript(value=Attribute(value=Name(id='df', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Name(id='SEGMENTS', ctx=Load()), Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_train_timestamp', ctx=Store())], value=Attribute(value=Name(id='fit_df', ctx=Load()), attr='index', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_train_init_dict', ctx=Store())], value=Dict(keys=[], values=[])), For(target=Name(id='current_segment', ctx=Store()), iter=Name(id='SEGMENTS', ctx=Load()), body=[Assign(targets=[Name(id='cur_series', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='fit_df', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Name(id='current_segment', ctx=Load()), Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load())), Assign(targets=[Name(id='cur_series', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='cur_series', ctx=Load()), attr='loc', ctx=Load()), slice=Slice(lower=Call(func=Attribute(value=Name(id='cur_series', ctx=Load()), attr='first_valid_index', ctx=Load()), args=[], keywords=[])), ctx=Load())), If(test=Compare(left=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='cur_series', ctx=Load()), attr='isna', ctx=Load()), args=[], keywords=[]), attr='sum', ctx=Load()), args=[], keywords=[]), ops=[Gt()], comparators=[Constant(value=0)]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[JoinedStr(values=[Constant(value='There should be no NaNs inside the segments')])], keywords=[]))], orelse=[]), Assign(targets=[Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_train_init_dict', ctx=Load()), slice=Name(id='current_segment', ctx=Load()), ctx=Store())], value=Subscript(value=Name(id='cur_series', ctx=Load()), slice=Slice(upper=Attribute(value=Name(id='self', ctx=Load()), attr='period', ctx=Load())), ctx=Load()))], orelse=[]), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_test_init_df', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='fit_df', ctx=Load()), attr='iloc', ctx=Load()), slice=Tuple(elts=[Slice(lower=UnaryOp(op=USub(), operand=Attribute(value=Name(id='self', ctx=Load()), attr='period', ctx=Load()))), Slice()], ctx=Load()), ctx=Load())), Assign(targets=[Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_test_init_df', ctx=Load()), attr='columns', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_test_init_df', ctx=Load()), attr='columns', ctx=Load()), attr='remove_unused_levels', ctx=Load()), args=[], keywords=[])), Return(value=Name(id='self', ctx=Load()))], decorator_list=[], returns=Constant(value='_SingleDifferencingTransform'))], decorator_list=[]), ClassDef(name='DifferencingTransform', bases=[Name(id='Transform', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='Calculate a time series differences.\n\nThis transform can work with NaNs at the bˉeginning of the segment, but fails when meets NaN insidɮe the segment.\n\nNotes\nϬ-----ơ\nTo understand how transform works we recommend:\n`Staϡtionari\x88ty andH Differencing <https:/Ţ/otexts.com/fpp2/stationarity.html>`_')), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='in_column', annotation=Name(id='str', ctx=Load())), arg(arg='period', annotation=Name(id='int', ctx=Load())), arg(arg='order', annotation=Name(id='int', ctx=Load())), arg(arg='inplace', annotation=Name(id='bool', ctx=Load())), arg(arg='out_column', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=1), Constant(value=1), Constant(value=True), Constant(value=None)]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Store())], value=Name(id='in_column', ctx=Load())), If(test=BoolOp(op=Or(), values=[UnaryOp(op=Not(), operand=Call(func=Name(id='isinstance', ctx=Load()), args=[Name(id='period', ctx=Load()), Name(id='int', ctx=Load())], keywords=[])), Compare(left=Name(id='period', ctx=Load()), ops=[Lt()], comparators=[Constant(value=1)])]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='Period should be at least 1')], keywords=[]))], orelse=[]), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='period', ctx=Store())], value=Name(id='period', ctx=Load())), If(test=BoolOp(op=Or(), values=[UnaryOp(op=Not(), operand=Call(func=Name(id='isinstance', ctx=Load()), args=[Name(id='order', ctx=Load()), Name(id='int', ctx=Load())], keywords=[])), Compare(left=Name(id='order', ctx=Load()), ops=[Lt()], comparators=[Constant(value=1)])]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='Order should be at least 1')], keywords=[]))], orelse=[]), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='order', ctx=Store())], value=Name(id='order', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='inplace', ctx=Store())], value=Name(id='inplace', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='out_column', ctx=Store())], value=Name(id='out_column', ctx=Load())), Assign(targets=[Name(id='result_out_column', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_get_column_name', ctx=Load()), args=[], keywords=[])), AnnAssign(target=Attribute(value=Name(id='self', ctx=Load()), attr='_differencing_transforms', ctx=Store()), annotation=Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='_SingleDifferencingTransform', ctx=Load()), ctx=Load()), value=List(elts=[], ctx=Load()), simple=0), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_differencing_transforms', ctx=Load()), attr='append', ctx=Load()), args=[Call(func=Name(id='_SingleDifferencingTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load())), keyword(arg='period', value=Attribute(value=Name(id='self', ctx=Load()), attr='period', ctx=Load())), keyword(arg='inplace', value=Attribute(value=Name(id='self', ctx=Load()), attr='inplace', ctx=Load())), keyword(arg='out_column', value=Name(id='result_out_column', ctx=Load()))])], keywords=[])), For(target=Name(id='_', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[BinOp(left=Attribute(value=Name(id='self', ctx=Load()), attr='order', ctx=Load()), op=Sub(), right=Constant(value=1))], keywords=[]), body=[Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_differencing_transforms', ctx=Load()), attr='append', ctx=Load()), args=[Call(func=Name(id='_SingleDifferencingTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Name(id='result_out_column', ctx=Load())), keyword(arg='period', value=Attribute(value=Name(id='self', ctx=Load()), attr='period', ctx=Load())), keyword(arg='inplace', value=Constant(value=True))])], keywords=[]))], orelse=[])], decorator_list=[]), FunctionDef(name='_get_column_name', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[If(test=Attribute(value=Name(id='self', ctx=Load()), attr='inplace', ctx=Load()), body=[Return(value=Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load()))], orelse=[]), If(test=Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='out_column', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Return(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='__repr__', ctx=Load()), args=[], keywords=[]))], orelse=[Return(value=Attribute(value=Name(id='self', ctx=Load()), attr='out_column', ctx=Load()))])], decorator_list=[], returns=Name(id='str', ctx=Load())), FunctionDef(name='fitCk', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='result_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='df', ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[])), For(target=Name(id='transform', ctx=Store()), iter=Attribute(value=Name(id='self', ctx=Load()), attr='_differencing_transforms', ctx=Load()), body=[Assign(targets=[Name(id='result_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='transform', ctx=Load()), attr='fit_transform', ctx=Load()), args=[Name(id='result_df', ctx=Load())], keywords=[]))], orelse=[]), Return(value=Name(id='self', ctx=Load()))], decorator_list=[], returns=Constant(value='DifferencingTransform')), FunctionDef(name='inverse_transform', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[If(test=UnaryOp(op=Not(), operand=Attribute(value=Name(id='self', ctx=Load()), attr='inplace', ctx=Load())), body=[Return(value=Name(id='df', ctx=Load()))], orelse=[]), Assign(targets=[Name(id='result_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='df', ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[])), For(target=Name(id='transform', ctx=Store()), iter=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_differencing_transforms', ctx=Load()), slice=Slice(step=UnaryOp(op=USub(), operand=Constant(value=1))), ctx=Load()), body=[Assign(targets=[Name(id='result_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='transform', ctx=Load()), attr='inverse_transform', ctx=Load()), args=[Name(id='result_df', ctx=Load())], keywords=[]))], orelse=[]), Return(value=Name(id='result_df', ctx=Load()))], decorator_list=[], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), FunctionDef(name='transform', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='result_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='df', ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[])), For(target=Name(id='transform', ctx=Store()), iter=Attribute(value=Name(id='self', ctx=Load()), attr='_differencing_transforms', ctx=Load()), body=[Assign(targets=[Name(id='result_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='transform', ctx=Load()), attr='transform', ctx=Load()), args=[Name(id='result_df', ctx=Load())], keywords=[]))], orelse=[]), Return(value=Name(id='result_df', ctx=Load()))], decorator_list=[], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], decorator_list=[])], type_ignores=[])