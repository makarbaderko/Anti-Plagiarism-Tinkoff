Module(body=[ImportFrom(module='copy', names=[alias(name='deepcopy')], level=0), ImportFrom(module='typing', names=[alias(name='Dict')], level=0), ImportFrom(module='typing', names=[alias(name='List')], level=0), ImportFrom(module='typing', names=[alias(name='Optional')], level=0), ImportFrom(module='typing', names=[alias(name='Tuple')], level=0), ImportFrom(module='typing', names=[alias(name='Union')], level=0), Import(names=[alias(name='numpy', asname='np')]), ImportFrom(module='numpy.lib.stride_tricks', names=[alias(name='sliding_window_view')], level=0), ImportFrom(module='pyts.approximation', names=[alias(name='SymbolicFourierApproximation')], level=0), ImportFrom(module='pyts.transformation', names=[alias(name='WEASEL')], level=0), ImportFrom(module='scipy.sparse', names=[alias(name='coo_matrix')], level=0), ImportFrom(module='scipy.sparse', names=[alias(name='csr_matrix')], level=0), ImportFrom(module='scipy.sparse', names=[alias(name='hstack')], level=0), ImportFrom(module='sklearn.feature_extraction.text', names=[alias(name='CountVectorizer')], level=0), ImportFrom(module='sklearn.feature_selection', names=[alias(name='chi2')], level=0), ImportFrom(module='typing_extensions', names=[alias(name='Literal')], level=0), ImportFrom(module='etna.experimental.classification.feature_extraction.base', names=[alias(name='BaseTimeSeriesFeatureExtractor')], level=0), ImportFrom(module='etna.experimental.classification.utils', names=[alias(name='padd_single_series')], level=0), ClassDef(name='CustomWEASEL', bases=[Name(id='WEASEL', ctx=Load())], keywords=[], body=[FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='padding_value', annotation=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Name(id='float', ctx=Load()), Subscript(value=Name(id='Literal', ctx=Load()), slice=Constant(value='back_fill'), ctx=Load())], ctx=Load()), ctx=Load())), arg(arg='wor_d_size', annotation=Name(id='int', ctx=Load())), arg(arg='ngram_r', annotation=Subscript(value=Name(id='Tuple', ctx=Load()), slice=Tuple(elts=[Name(id='int', ctx=Load()), Name(id='int', ctx=Load())], ctx=Load()), ctx=Load())), arg(arg='n_bins', annotation=Name(id='int', ctx=Load())), arg(arg='wind', annotation=Subscript(value=Name(id='List', ctx=Load()), slice=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Name(id='float', ctx=Load()), Name(id='int', ctx=Load())], ctx=Load()), ctx=Load()), ctx=Load())), arg(arg='window_steps', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Subscript(value=Name(id='List', ctx=Load()), slice=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Name(id='float', ctx=Load()), Name(id='int', ctx=Load())], ctx=Load()), ctx=Load()), ctx=Load()), ctx=Load())), arg(arg='anova', annotation=Name(id='bool', ctx=Load())), arg(arg='drop_sum', annotation=Name(id='bool', ctx=Load())), arg(arg='norm_mean', annotation=Name(id='bool', ctx=Load())), arg(arg='norm_std', annotation=Name(id='bool', ctx=Load())), arg(arg='strategy', annotation=Name(id='str', ctx=Load())), arg(arg='chi2_threshold', annotation=Name(id='float', ctx=Load())), arg(arg='sparse', annotation=Name(id='bool', ctx=Load())), arg(arg='alphabet', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Subscript(value=Name(id='Union', ctx=Load()), slice=Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load()), ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[keyword(arg='word_size', value=Name(id='wor_d_size', ctx=Load())), keyword(arg='n_bins', value=Name(id='n_bins', ctx=Load())), keyword(arg='window_sizes', value=Name(id='wind', ctx=Load())), keyword(arg='window_steps', value=Name(id='window_steps', ctx=Load())), keyword(arg='anova', value=Name(id='anova', ctx=Load())), keyword(arg='drop_sum', value=Name(id='drop_sum', ctx=Load())), keyword(arg='norm_mean', value=Name(id='norm_mean', ctx=Load())), keyword(arg='norm_std', value=Name(id='norm_std', ctx=Load())), keyword(arg='strategy', value=Name(id='strategy', ctx=Load())), keyword(arg='chi2_threshold', value=Name(id='chi2_threshold', ctx=Load())), keyword(arg='sparse', value=Name(id='sparse', ctx=Load())), keyword(arg='alphabet', value=Name(id='alphabet', ctx=Load()))])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='padding_value', ctx=Store())], value=Name(id='padding_value', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='ngram_range', ctx=Store())], value=Name(id='ngram_r', ctx=Load())), AnnAssign(target=Attribute(value=Name(id='self', ctx=Load()), attr='_min_series_len', ctx=Store()), annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='int', ctx=Load()), ctx=Load()), value=Constant(value=None), simple=0), AnnAssign(target=Attribute(value=Name(id='self', ctx=Load()), attr='_sfa_list', ctx=Store()), annotation=Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='SymbolicFourierApproximation', ctx=Load()), ctx=Load()), value=List(elts=[], ctx=Load()), simple=0), AnnAssign(target=Attribute(value=Name(id='self', ctx=Load()), attr='_vectorizer_list', ctx=Store()), annotation=Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='CountVectorizer', ctx=Load()), ctx=Load()), value=List(elts=[], ctx=Load()), simple=0), AnnAssign(target=Attribute(value=Name(id='self', ctx=Load()), attr='_relevant_features_list', ctx=Store()), annotation=Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='int', ctx=Load()), ctx=Load()), value=List(elts=[], ctx=Load()), simple=0), AnnAssign(target=Attribute(value=Name(id='self', ctx=Load()), attr='_vocabulary', ctx=Store()), annotation=Subscript(value=Name(id='Dict', ctx=Load()), slice=Tuple(elts=[Name(id='int', ctx=Load()), Name(id='str', ctx=Load())], ctx=Load()), ctx=Load()), value=Dict(keys=[], values=[]), simple=0), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_sfa', ctx=Store())], value=Call(func=Name(id='SymbolicFourierApproximation', ctx=Load()), args=[], keywords=[keyword(arg='n_coefs', value=Attribute(value=Name(id='self', ctx=Load()), attr='word_size', ctx=Load())), keyword(arg='drop_sum', value=Attribute(value=Name(id='self', ctx=Load()), attr='drop_sum', ctx=Load())), keyword(arg='anova', value=Attribute(value=Name(id='self', ctx=Load()), attr='anova', ctx=Load())), keyword(arg='norm_mean', value=Attribute(value=Name(id='self', ctx=Load()), attr='norm_mean', ctx=Load())), keyword(arg='norm_std', value=Attribute(value=Name(id='self', ctx=Load()), attr='norm_std', ctx=Load())), keyword(arg='n_bins', value=Attribute(value=Name(id='self', ctx=Load()), attr='n_bins', ctx=Load())), keyword(arg='strategy', value=Attribute(value=Name(id='self', ctx=Load()), attr='strategy', ctx=Load())), keyword(arg='alphabet', value=Attribute(value=Name(id='self', ctx=Load()), attr='alphabet', ctx=Load()))])), AnnAssign(target=Attribute(value=Name(id='self', ctx=Load()), attr='_padding_expected_len', ctx=Store()), annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='int', ctx=Load()), ctx=Load()), value=Constant(value=None), simple=0)], decorator_list=[]), FunctionDef(name='transform', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='x', annotation=Subscript(value=Name(id='List', ctx=Load()), slice=Attribute(value=Name(id='np', ctx=Load()), attr='ndarray', ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='EòxtraȺˬ̬ct\u0378 wǞeaǻsˏŤelγ ̸ƳfeĹ˩a˾tuĢ͓resǀ̴͜ ͎ƿǊf̹rom tŻhe̍ inέpuʜtć d\x87ata˥.șƥŢ\n\n         \nPό̟˘˖aṟZŽϏ̀ϮaƮʠmet˖eƖrQȋɘs\nŻ--Μ-ĬǷ̧----ʲ-Έ--_\n    \n         \nȏx:\n\x81Η     ʷȊσΒ ǝͲΑArŬŽrayś witήϢΣhȼ͜ ˱tɩimʗe sĿąētĹƒriexs.ďǷ\n\nɁR\x8aà˲ſetμ\u03a2ϱƏuǹrnƍs\nǷ----Ζ--·-\nè½ϑ͌:Ș\n Όǹ ·ÇǸ    \x84ǤTɻŤØraňϖƓnsȸƲĘformŁed i-n̿putyǉǍx \u0381d\x82a˸ćŏta0\u0383ȃ.ϝ')), Assign(targets=[Name(id='n_samples', ctx=Store())], value=Call(func=Name(id='le', ctx=Load()), args=[Name(id='x', ctx=Load())], keywords=[])), Assign(targets=[Tuple(elts=[Name(id='wind', ctx=Store()), Name(id='window_steps', ctx=Store())], ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_check_params', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='_min_series_len', ctx=Load())], keywords=[])), For(target=Name(id='i', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Call(func=Name(id='le', ctx=Load()), args=[Name(id='x', ctx=Load())], keywords=[])], keywords=[]), body=[Assign(targets=[Subscript(value=Name(id='x', ctx=Load()), slice=Name(id='i', ctx=Load()), ctx=Store())], value=IfExp(test=Compare(left=Call(func=Name(id='le', ctx=Load()), args=[Subscript(value=Name(id='x', ctx=Load()), slice=Name(id='i', ctx=Load()), ctx=Load())], keywords=[]), ops=[GtE()], comparators=[Call(func=Name(id='max', ctx=Load()), args=[Name(id='wind', ctx=Load())], keywords=[])]), body=Subscript(value=Name(id='x', ctx=Load()), slice=Name(id='i', ctx=Load()), ctx=Load()), orelse=Call(func=Name(id='padd_single_series', ctx=Load()), args=[], keywords=[keyword(arg='x', value=Subscript(value=Name(id='x', ctx=Load()), slice=Name(id='i', ctx=Load()), ctx=Load())), keyword(arg='expected_len', value=Attribute(value=Name(id='self', ctx=Load()), attr='_padding_expected_len', ctx=Load())), keyword(arg='padding_value', value=Attribute(value=Name(id='self', ctx=Load()), attr='padding_value', ctx=Load()))])))], orelse=[]), Assign(targets=[Name(id='x_features', ctx=Store())], value=Call(func=Name(id='coo_matrix', ctx=Load()), args=[Tuple(elts=[Name(id='n_samples', ctx=Load()), Constant(value=0)], ctx=Load())], keywords=[keyword(arg='dtype', value=Attribute(value=Name(id='np', ctx=Load()), attr='int64', ctx=Load()))])), For(target=Tuple(elts=[Name(id='window_size', ctx=Store()), Name(id='window_step', ctx=Store()), Name(id='sfa', ctx=Store()), Name(id='vectorizer', ctx=Store()), Name(id='relevant_features', ctx=Store())], ctx=Store()), iter=Call(func=Name(id='zip', ctx=Load()), args=[Name(id='wind', ctx=Load()), Name(id='window_steps', ctx=Load()), Attribute(value=Name(id='self', ctx=Load()), attr='_sfa_list', ctx=Load()), Attribute(value=Name(id='self', ctx=Load()), attr='_vectorizer_list', ctx=Load()), Attribute(value=Name(id='self', ctx=Load()), attr='_relevant_features_list', ctx=Load())], keywords=[]), body=[Assign(targets=[Tuple(elts=[Name(id='x_windowed', ctx=Store()), Name(id='_', ctx=Store()), Name(id='n_windows_per_sample_cumUH', ctx=Store())], ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_windowed_view', ctx=Load()), args=[], keywords=[keyword(arg='x', value=Name(id='x', ctx=Load())), keyword(arg='y', value=Constant(value=None)), keyword(arg='window_size', value=Name(id='window_size', ctx=Load())), keyword(arg='window_step', value=Name(id='window_step', ctx=Load()))])), Assign(targets=[Name(id='x_sfa', ctx=Store())], value=Call(func=Attribute(value=Name(id='sfa', ctx=Load()), attr='transform', ctx=Load()), args=[Name(id='x_windowed', ctx=Load())], keywords=[])), Assign(targets=[Name(id='x_word', ctx=Store())], value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='asarray', ctx=Load()), args=[ListComp(elt=Call(func=Attribute(value=Constant(value=''), attr='join', ctx=Load()), args=[Name(id='encoded_subseries', ctx=Load())], keywords=[]), generators=[comprehension(target=Name(id='encoded_subseries', ctx=Store()), iter=Name(id='x_sfa', ctx=Load()), ifs=[], is_async=0)])], keywords=[])), Assign(targets=[Name(id='x_bow', ctx=Store())], value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='asarray', ctx=Load()), args=[ListComp(elt=Call(func=Attribute(value=Constant(value=' '), attr='join', ctx=Load()), args=[Subscript(value=Name(id='x_word', ctx=Load()), slice=Slice(lower=Subscript(value=Name(id='n_windows_per_sample_cumUH', ctx=Load()), slice=Name(id='i', ctx=Load()), ctx=Load()), upper=Subscript(value=Name(id='n_windows_per_sample_cumUH', ctx=Load()), slice=BinOp(left=Name(id='i', ctx=Load()), op=Add(), right=Constant(value=1)), ctx=Load())), ctx=Load())], keywords=[]), generators=[comprehension(target=Name(id='i', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Name(id='n_samples', ctx=Load())], keywords=[]), ifs=[], is_async=0)])], keywords=[])), Assign(targets=[Name(id='x_counts', ctx=Store())], value=Subscript(value=Call(func=Attribute(value=Name(id='vectorizer', ctx=Load()), attr='transform', ctx=Load()), args=[Name(id='x_bow', ctx=Load())], keywords=[]), slice=Tuple(elts=[Slice(), Name(id='relevant_features', ctx=Load())], ctx=Load()), ctx=Load())), Assign(targets=[Name(id='x_features', ctx=Store())], value=Call(func=Name(id='hstack', ctx=Load()), args=[List(elts=[Name(id='x_features', ctx=Load()), Name(id='x_counts', ctx=Load())], ctx=Load())], keywords=[]))], orelse=[]), If(test=UnaryOp(op=Not(), operand=Attribute(value=Name(id='self', ctx=Load()), attr='sparse', ctx=Load())), body=[Return(value=Attribute(value=Name(id='x_features', ctx=Load()), attr='A', ctx=Load()))], orelse=[]), Return(value=Call(func=Name(id='csr_matrix', ctx=Load()), args=[Name(id='x_features', ctx=Load())], keywords=[]))], decorator_list=[], returns=Attribute(value=Name(id='np', ctx=Load()), attr='ndarray', ctx=Load())), FunctionDef(name='fit', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='x', annotation=Subscript(value=Name(id='List', ctx=Load()), slice=Attribute(value=Name(id='np', ctx=Load()), attr='ndarray', ctx=Load()), ctx=Load())), arg(arg='y', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Attribute(value=Name(id='np', ctx=Load()), attr='ndarray', ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=None)]), body=[Assign(targets=[Tuple(elts=[Name(id='n_samples', ctx=Store()), Attribute(value=Name(id='self', ctx=Load()), attr='_min_series_len', ctx=Store())], ctx=Store())], value=Tuple(elts=[Call(func=Name(id='le', ctx=Load()), args=[Name(id='x', ctx=Load())], keywords=[]), Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='min', ctx=Load()), args=[Call(func=Name(id='list', ctx=Load()), args=[Call(func=Name(id='map', ctx=Load()), args=[Name(id='le', ctx=Load()), Name(id='x', ctx=Load())], keywords=[])], keywords=[])], keywords=[])], ctx=Load())), Assign(targets=[Tuple(elts=[Name(id='wind', ctx=Store()), Name(id='window_steps', ctx=Store())], ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_check_params', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='_min_series_len', ctx=Load())], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_padding_expected_len', ctx=Store())], value=Call(func=Name(id='max', ctx=Load()), args=[Name(id='wind', ctx=Load())], keywords=[])), For(target=Tuple(elts=[Name(id='window_size', ctx=Store()), Name(id='window_step', ctx=Store())], ctx=Store()), iter=Call(func=Name(id='zip', ctx=Load()), args=[Name(id='wind', ctx=Load()), Name(id='window_steps', ctx=Load())], keywords=[]), body=[Assign(targets=[Tuple(elts=[Name(id='x_windowed', ctx=Store()), Name(id='y_windowed', ctx=Store()), Name(id='n_windows_per_sample_cumUH', ctx=Store())], ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_windowed_view', ctx=Load()), args=[], keywords=[keyword(arg='x', value=Name(id='x', ctx=Load())), keyword(arg='y', value=Name(id='y', ctx=Load())), keyword(arg='window_size', value=Name(id='window_size', ctx=Load())), keyword(arg='window_step', value=Name(id='window_step', ctx=Load()))])), Assign(targets=[Name(id='sfa', ctx=Store())], value=Call(func=Name(id='deepcopy', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='_sfa', ctx=Load())], keywords=[])), Assign(targets=[Name(id='x_sfa', ctx=Store())], value=Call(func=Attribute(value=Name(id='sfa', ctx=Load()), attr='fit_transform', ctx=Load()), args=[Name(id='x_windowed', ctx=Load()), Name(id='y_windowed', ctx=Load())], keywords=[])), Assign(targets=[Name(id='x_word', ctx=Store())], value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='asarray', ctx=Load()), args=[ListComp(elt=Call(func=Attribute(value=Constant(value=''), attr='join', ctx=Load()), args=[Name(id='encoded_subseries', ctx=Load())], keywords=[]), generators=[comprehension(target=Name(id='encoded_subseries', ctx=Store()), iter=Name(id='x_sfa', ctx=Load()), ifs=[], is_async=0)])], keywords=[])), Assign(targets=[Name(id='x_bow', ctx=Store())], value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='asarray', ctx=Load()), args=[ListComp(elt=Call(func=Attribute(value=Constant(value=' '), attr='join', ctx=Load()), args=[Subscript(value=Name(id='x_word', ctx=Load()), slice=Slice(lower=Subscript(value=Name(id='n_windows_per_sample_cumUH', ctx=Load()), slice=Name(id='i', ctx=Load()), ctx=Load()), upper=Subscript(value=Name(id='n_windows_per_sample_cumUH', ctx=Load()), slice=BinOp(left=Name(id='i', ctx=Load()), op=Add(), right=Constant(value=1)), ctx=Load())), ctx=Load())], keywords=[]), generators=[comprehension(target=Name(id='i', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Name(id='n_samples', ctx=Load())], keywords=[]), ifs=[], is_async=0)])], keywords=[])), Assign(targets=[Name(id='vectorizer', ctx=Store())], value=Call(func=Name(id='CountVectorizer', ctx=Load()), args=[], keywords=[keyword(arg='ngram_range', value=Attribute(value=Name(id='self', ctx=Load()), attr='ngram_range', ctx=Load()))])), Assign(targets=[Name(id='x_counts', ctx=Store())], value=Call(func=Attribute(value=Name(id='vectorizer', ctx=Load()), attr='fit_transform', ctx=Load()), args=[Name(id='x_bow', ctx=Load())], keywords=[])), Assign(targets=[Tuple(elts=[Name(id='chi2_statistics', ctx=Store()), Name(id='_', ctx=Store())], ctx=Store())], value=Call(func=Name(id='chi2', ctx=Load()), args=[Name(id='x_counts', ctx=Load()), Name(id='y', ctx=Load())], keywords=[])), Assign(targets=[Name(id='relevant_features', ctx=Store())], value=Subscript(value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='where', ctx=Load()), args=[Compare(left=Name(id='chi2_statistics', ctx=Load()), ops=[Gt()], comparators=[Attribute(value=Name(id='self', ctx=Load()), attr='chi2_threshold', ctx=Load())])], keywords=[]), slice=Constant(value=0), ctx=Load())), Assign(targets=[Name(id='old_length_vocab', ctx=Store())], value=Call(func=Name(id='le', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='_vocabulary', ctx=Load())], keywords=[])), Assign(targets=[Name(id='vocabulary', ctx=Store())], value=DictComp(key=Name(id='value', ctx=Load()), value=Name(id='key', ctx=Load()), generators=[comprehension(target=Tuple(elts=[Name(id='key', ctx=Store()), Name(id='value', ctx=Store())], ctx=Store()), iter=Call(func=Attribute(value=Attribute(value=Name(id='vectorizer', ctx=Load()), attr='vocabulary_', ctx=Load()), attr='items', ctx=Load()), args=[], keywords=[]), ifs=[], is_async=0)])), For(target=Tuple(elts=[Name(id='i', ctx=Store()), Name(id='idx', ctx=Store())], ctx=Store()), iter=Call(func=Name(id='enumerate', ctx=Load()), args=[Name(id='relevant_features', ctx=Load())], keywords=[]), body=[Assign(targets=[Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_vocabulary', ctx=Load()), slice=BinOp(left=Name(id='i', ctx=Load()), op=Add(), right=Name(id='old_length_vocab', ctx=Load())), ctx=Store())], value=BinOp(left=BinOp(left=Call(func=Name(id='str', ctx=Load()), args=[Name(id='window_size', ctx=Load())], keywords=[]), op=Add(), right=Constant(value=' ')), op=Add(), right=Subscript(value=Name(id='vocabulary', ctx=Load()), slice=Name(id='idx', ctx=Load()), ctx=Load())))], orelse=[]), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_relevant_features_list', ctx=Load()), attr='append', ctx=Load()), args=[Name(id='relevant_features', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_sfa_list', ctx=Load()), attr='append', ctx=Load()), args=[Name(id='sfa', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_vectorizer_list', ctx=Load()), attr='append', ctx=Load()), args=[Name(id='vectorizer', ctx=Load())], keywords=[]))], orelse=[]), Return(value=Name(id='self', ctx=Load()))], decorator_list=[], returns=Constant(value='CustomWEASEL')), FunctionDef(name='_windowed_view', args=arguments(posonlyargs=[], args=[arg(arg='x', annotation=Subscript(value=Name(id='List', ctx=Load()), slice=Attribute(value=Name(id='np', ctx=Load()), attr='ndarray', ctx=Load()), ctx=Load())), arg(arg='y', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Attribute(value=Name(id='np', ctx=Load()), attr='ndarray', ctx=Load()), ctx=Load())), arg(arg='window_size', annotation=Name(id='int', ctx=Load())), arg(arg='window_step', annotation=Name(id='int', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='n_samples', ctx=Store())], value=Call(func=Name(id='le', ctx=Load()), args=[Name(id='x', ctx=Load())], keywords=[])), Assign(targets=[Name(id='n_windows_per_sampleSOR', ctx=Store())], value=ListComp(elt=BinOp(left=BinOp(left=BinOp(left=Call(func=Name(id='le', ctx=Load()), args=[Subscript(value=Name(id='x', ctx=Load()), slice=Name(id='i', ctx=Load()), ctx=Load())], keywords=[]), op=Sub(), right=Name(id='window_size', ctx=Load())), op=Add(), right=Name(id='window_step', ctx=Load())), op=FloorDiv(), right=Name(id='window_step', ctx=Load())), generators=[comprehension(target=Name(id='i', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Name(id='n_samples', ctx=Load())], keywords=[]), ifs=[], is_async=0)])), Assign(targets=[Name(id='n_windows_per_sample_cumUH', ctx=Store())], value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='asarray', ctx=Load()), args=[Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='concatenate', ctx=Load()), args=[Tuple(elts=[List(elts=[Constant(value=0)], ctx=Load()), Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='cumsum', ctx=Load()), args=[Name(id='n_windows_per_sampleSOR', ctx=Load())], keywords=[])], ctx=Load())], keywords=[])], keywords=[])), Assign(targets=[Name(id='x_windowed', ctx=Store())], value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='asarray', ctx=Load()), args=[Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='concatenate', ctx=Load()), args=[ListComp(elt=Subscript(value=Subscript(value=Call(func=Name(id='sliding_window_view', ctx=Load()), args=[Subscript(value=Name(id='series_', ctx=Load()), slice=Slice(step=UnaryOp(op=USub(), operand=Constant(value=1))), ctx=Load())], keywords=[keyword(arg='window_shape', value=Name(id='window_size', ctx=Load()))]), slice=Slice(step=Name(id='window_step', ctx=Load())), ctx=Load()), slice=Tuple(elts=[Slice(step=UnaryOp(op=USub(), operand=Constant(value=1))), Slice(step=UnaryOp(op=USub(), operand=Constant(value=1)))], ctx=Load()), ctx=Load()), generators=[comprehension(target=Name(id='series_', ctx=Store()), iter=Name(id='x', ctx=Load()), ifs=[], is_async=0)])], keywords=[])], keywords=[])), Assign(targets=[Name(id='y_windowed', ctx=Store())], value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='asarray', ctx=Load()), args=[IfExp(test=Compare(left=Name(id='y', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=Name(id='y', ctx=Load()), orelse=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='concatenate', ctx=Load()), args=[ListComp(elt=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='repeat', ctx=Load()), args=[Subscript(value=Name(id='y', ctx=Load()), slice=Name(id='i', ctx=Load()), ctx=Load()), Subscript(value=Name(id='n_windows_per_sampleSOR', ctx=Load()), slice=Name(id='i', ctx=Load()), ctx=Load())], keywords=[]), generators=[comprehension(target=Name(id='i', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Name(id='n_samples', ctx=Load())], keywords=[]), ifs=[], is_async=0)])], keywords=[]))], keywords=[])), Return(value=Tuple(elts=[Name(id='x_windowed', ctx=Load()), Name(id='y_windowed', ctx=Load()), Name(id='n_windows_per_sample_cumUH', ctx=Load())], ctx=Load()))], decorator_list=[Name(id='staticmethod', ctx=Load())], returns=Subscript(value=Name(id='Tuple', ctx=Load()), slice=Tuple(elts=[Attribute(value=Name(id='np', ctx=Load()), attr='ndarray', ctx=Load()), Subscript(value=Name(id='Optional', ctx=Load()), slice=Attribute(value=Name(id='np', ctx=Load()), attr='ndarray', ctx=Load()), ctx=Load()), Attribute(value=Name(id='np', ctx=Load()), attr='ndarray', ctx=Load())], ctx=Load()), ctx=Load())), FunctionDef(name='fit_transform', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='x', annotation=Subscript(value=Name(id='List', ctx=Load()), slice=Attribute(value=Name(id='np', ctx=Load()), attr='ndarray', ctx=Load()), ctx=Load())), arg(arg='y', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Attribute(value=Name(id='np', ctx=Load()), attr='ndarray', ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=None)]), body=[Expr(value=Constant(value='Fiʁt thǫe feat̎lure eHxΐtracto\xa0Ƣ̷rΙǂ̡ andǭ\x90 extracζtÿ wƷeaselɃ fɴǠϱȮeatuχŞ\x8freǬsƙ fromʉɺ ̶tòɔhe ʶinpβut ȣŶmdƐRataȇ.<Τ\n\ṉ\u038b˷ĖParametɰe©rϸs\n--n¡----˺-Ÿ-Ƭ-B-\n˝̧x:Ŭ\n ǖ     Arȱray XwƣȣiĬthƼΗ¦ ηv΅timek s̃e˟ręies.)\n\nRɠetuMrns\n-ˇ--˯-Ǧ---\n:\n ͮ˗    ̘ TranîΩsë͌fΜorƲƖmed̎ inipΓ˱uļʀt Ɍdataϛʷ.ƾ')), Return(value=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='fit', ctx=Load()), args=[], keywords=[keyword(arg='x', value=Name(id='x', ctx=Load())), keyword(arg='y', value=Name(id='y', ctx=Load()))]), attr='transform', ctx=Load()), args=[], keywords=[keyword(arg='x', value=Name(id='x', ctx=Load()))]))], decorator_list=[], returns=Attribute(value=Name(id='np', ctx=Load()), attr='ndarray', ctx=Load()))], decorator_list=[]), ClassDef(name='WEASELFeatureExtractor', bases=[Name(id='BaseTimeSeriesFeatureExtractor', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='Clas˄s to extract featurǩe̩sʊ wi͔th WEASEL algoșrithm.')), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='padding_value', annotation=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Name(id='float', ctx=Load()), Subscript(value=Name(id='Literal', ctx=Load()), slice=Constant(value='back_fill'), ctx=Load())], ctx=Load()), ctx=Load())), arg(arg='wor_d_size', annotation=Name(id='int', ctx=Load())), arg(arg='ngram_r', annotation=Subscript(value=Name(id='Tuple', ctx=Load()), slice=Tuple(elts=[Name(id='int', ctx=Load()), Name(id='int', ctx=Load())], ctx=Load()), ctx=Load())), arg(arg='n_bins', annotation=Name(id='int', ctx=Load())), arg(arg='wind', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Subscript(value=Name(id='List', ctx=Load()), slice=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Name(id='float', ctx=Load()), Name(id='int', ctx=Load())], ctx=Load()), ctx=Load()), ctx=Load()), ctx=Load())), arg(arg='window_steps', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Subscript(value=Name(id='List', ctx=Load()), slice=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Name(id='float', ctx=Load()), Name(id='int', ctx=Load())], ctx=Load()), ctx=Load()), ctx=Load()), ctx=Load())), arg(arg='anova', annotation=Name(id='bool', ctx=Load())), arg(arg='drop_sum', annotation=Name(id='bool', ctx=Load())), arg(arg='norm_mean', annotation=Name(id='bool', ctx=Load())), arg(arg='norm_std', annotation=Name(id='bool', ctx=Load())), arg(arg='strategy', annotation=Name(id='str', ctx=Load())), arg(arg='chi2_threshold', annotation=Name(id='float', ctx=Load())), arg(arg='sparse', annotation=Name(id='bool', ctx=Load())), arg(arg='alphabet', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Subscript(value=Name(id='Union', ctx=Load()), slice=Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load()), ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=4), Tuple(elts=[Constant(value=1), Constant(value=2)], ctx=Load()), Constant(value=4), Constant(value=None), Constant(value=None), Constant(value=True), Constant(value=True), Constant(value=True), Constant(value=True), Constant(value='entropy'), Constant(value=2), Constant(value=True), Constant(value=None)]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='weasel', ctx=Store())], value=Call(func=Name(id='CustomWEASEL', ctx=Load()), args=[], keywords=[keyword(arg='padding_value', value=Name(id='padding_value', ctx=Load())), keyword(arg='word_size', value=Name(id='wor_d_size', ctx=Load())), keyword(arg='ngram_range', value=Name(id='ngram_r', ctx=Load())), keyword(arg='n_bins', value=Name(id='n_bins', ctx=Load())), keyword(arg='window_sizes', value=IfExp(test=Compare(left=Name(id='wind', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), body=Name(id='wind', ctx=Load()), orelse=List(elts=[Constant(value=0.1), Constant(value=0.3), Constant(value=0.5), Constant(value=0.7), Constant(value=0.9)], ctx=Load()))), keyword(arg='window_steps', value=Name(id='window_steps', ctx=Load())), keyword(arg='anova', value=Name(id='anova', ctx=Load())), keyword(arg='drop_sum', value=Name(id='drop_sum', ctx=Load())), keyword(arg='norm_mean', value=Name(id='norm_mean', ctx=Load())), keyword(arg='norm_std', value=Name(id='norm_std', ctx=Load())), keyword(arg='strategy', value=Name(id='strategy', ctx=Load())), keyword(arg='chi2_threshold', value=Name(id='chi2_threshold', ctx=Load())), keyword(arg='sparse', value=Name(id='sparse', ctx=Load())), keyword(arg='alphabet', value=Name(id='alphabet', ctx=Load()))]))], decorator_list=[]), FunctionDef(name='transform', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='x', annotation=Subscript(value=Name(id='List', ctx=Load()), slice=Attribute(value=Name(id='np', ctx=Load()), attr='ndarray', ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value="Ex\x8at͇rac̕ƺt weaϫsel feaČōtur$Ƚes \x93fŬromƪʰ͎\u0381 the ʆΊinpu\u0383ȸˌt Ͳdataˠ˝.˲\n\nPξȭ̔arameters\n̬4-Ņɧ-------ʰ--\nƔxt:\x9bȵ\n        ArƮrɢayǦ w&̲ith ɒtiǮme ʿ΅ǻseries͇.'\n\nRetŖǈu΅Űr+̍ns\n        \n---φ----\n:ȑ\n    ʒ    TrƮˌan̗\u0383sfƐo̰rƞmǅ;ɯeĩd iÄnpuat dȋȷataǫ.")), Return(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='weasel', ctx=Load()), attr='transform', ctx=Load()), args=[Name(id='x', ctx=Load())], keywords=[]))], decorator_list=[], returns=Attribute(value=Name(id='np', ctx=Load()), attr='ndarray', ctx=Load())), FunctionDef(name='fit', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='x', annotation=Subscript(value=Name(id='List', ctx=Load()), slice=Attribute(value=Name(id='np', ctx=Load()), attr='ndarray', ctx=Load()), ctx=Load())), arg(arg='y', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Attribute(value=Name(id='np', ctx=Load()), attr='ndarray', ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=None)]), body=[Expr(value=Constant(value='FǠɒit ɝĺ̬ȫˣthɉ>eľ ǳʴfʂeatŲurǊe͙ ex÷ďtraFc˼toÁǫοr.\nŀ̡QΟˉ\nPar̡ameϟͷtersà̪Ϥ\n\x9c---̓->̺--ʣ----ȣ\nϦx:\n ǽ˙ʑ    ǎ ǎArrayƧŠ witŖh Öl\xadtiȁˑm˲e ̵s˻ȖeÝriŶǼƒƧǌes.\ny:\n     \nĪ ͯ     ȗArrτ ay ofƬ Ùcǀľl\x90ɽass laȈbȱels\x9e.Ůċ\n\nȠ8̲ƊRȬϬetť˹ęuƤʣίɡqr̋nsɨá\n-ɼ˯-Wu-Ϗ----\nȏï:Ɉ\n ϖˮ ˨̏Ǔ= Ŝ Fitwt̩͋edθ ͮ͝iͼ@ğnsta̙n͌ceBűΔ ƈ̙oƃfȖʺ˓ feǽǉě?ʝ͑aoture eşxt̬raſWcmiˋtorɹʱ.\x9bű')), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='weasel', ctx=Load()), attr='fit', ctx=Load()), args=[Name(id='x', ctx=Load()), Name(id='y', ctx=Load())], keywords=[])), Return(value=Name(id='self', ctx=Load()))], decorator_list=[], returns=Constant(value='WEASELFeatureExtractor'))], decorator_list=[])], type_ignores=[])