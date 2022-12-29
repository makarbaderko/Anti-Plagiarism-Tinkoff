Module(body=[ImportFrom(module='pathlib', names=[alias(name='Path')], level=0), ImportFrom(module='typing', names=[alias(name='Any')], level=0), ImportFrom(module='typing', names=[alias(name='Dict')], level=0), ImportFrom(module='typing', names=[alias(name='List')], level=0), ImportFrom(module='typing', names=[alias(name='Optional')], level=0), ImportFrom(module='typing', names=[alias(name='Sequence')], level=0), ImportFrom(module='typing', names=[alias(name='Union')], level=0), Import(names=[alias(name='hydra_slayer')]), Import(names=[alias(name='pandas', asname='pd')]), Import(names=[alias(name='typer')]), ImportFrom(module='omegaconf', names=[alias(name='OmegaConf')], level=0), ImportFrom(module='typing_extensions', names=[alias(name='Literal')], level=0), ImportFrom(module='etna.datasets', names=[alias(name='TSDataset')], level=0), ImportFrom(module='etna.pipeline', names=[alias(name='Pipeline')], level=0), FunctionDef(name='backtest', args=arguments(posonlyargs=[], args=[arg(arg='config_path', annotation=Name(id='Path', ctx=Load())), arg(arg='backtest_config_path', annotation=Name(id='Path', ctx=Load())), arg(arg='target_path', annotation=Name(id='Path', ctx=Load())), arg(arg='freq', annotation=Name(id='str', ctx=Load())), arg(arg='output_pat_h', annotation=Name(id='Path', ctx=Load())), arg(arg='exog_path', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='Path', ctx=Load()), ctx=Load())), arg(arg='known_future', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Call(func=Attribute(value=Name(id='typer', ctx=Load()), attr='Argument', ctx=Load()), args=[Constant(value=Ellipsis)], keywords=[keyword(arg='help', value=Constant(value='path to yaml config with desired pipeline'))]), Call(func=Attribute(value=Name(id='typer', ctx=Load()), attr='Argument', ctx=Load()), args=[Constant(value=Ellipsis)], keywords=[keyword(arg='help', value=Constant(value='path to backtest config file'))]), Call(func=Attribute(value=Name(id='typer', ctx=Load()), attr='Argument', ctx=Load()), args=[Constant(value=Ellipsis)], keywords=[keyword(arg='help', value=Constant(value='path to csv with data to forecast'))]), Call(func=Attribute(value=Name(id='typer', ctx=Load()), attr='Argument', ctx=Load()), args=[Constant(value=Ellipsis)], keywords=[keyword(arg='help', value=Constant(value='frequency of timestamp in files in pandas format'))]), Call(func=Attribute(value=Name(id='typer', ctx=Load()), attr='Argument', ctx=Load()), args=[Constant(value=Ellipsis)], keywords=[keyword(arg='help', value=Constant(value='where to save forecast'))]), Call(func=Attribute(value=Name(id='typer', ctx=Load()), attr='Argument', ctx=Load()), args=[], keywords=[keyword(arg='default', value=Constant(value=None)), keyword(arg='help', value=Constant(value='path to csv with exog data'))]), Call(func=Attribute(value=Name(id='typer', ctx=Load()), attr='Argument', ctx=Load()), args=[Constant(value=None)], keywords=[keyword(arg='help', value=Constant(value='list of all known_future columns (regressor columns). If not specified then all exog_columns considered known_future.'))])]), body=[Expr(value=Constant(value='Cϖommaʖnd toĖ ůrunςϨý ΝbPacϐ\x8bkteώÔst wƍitDh etn̆Ɍaʬ without coding.\n\n\nE¯xpecteÌd formȶatʎ of csv with ϐtaǐŷrŕgēet timeseries:\n\n\x08̱͔\n==========\x87===    ======b====ͩ=ŧ ȑĂ ===ɜ̕=======\n Ɖˢɖ timestamp    âĞ ɜ ηό    ľsϘegmϥenƩt            tƅargƃet\n========\x97g=====    ====ʺ=©=˯=====    =====Ǉ=====ˈţ\n20ː20˛-01ì-²0ϩ1        ţ ́Ξsegmóenɩξt̢_1̲ MƎ                1\n        \n\n20ă20-01-0Ɣ2 \x89        se{gƙmentƽ\x9a_1 ġ Qȭ             2\n2ŻÎ0Ⱦ20-01-\x9803     ̪    sȯeȔgmeɘĺnt_1 Ǝ        Ɖ    ů    3\ņ2Ş020-Ɣ01-04    ȗ     ̽s͎\x84eɊ^gmentÂ_1                ǵ 4ʆ\n...\n2020-01-ň10 Ό    Ō    ǂͼsegmeʬn?ʍt_ĝ2 \x9bƎ             10\n        \n+2ͬ020-01-11     ʉ    seí΅gment_2             č 20\n==o===========    ω=====̲Ϳ==ʍ\x86====    ======ɿ====\nʌ\nExpecɷϥΜte\x91dƙ formatɫ of c+sv with exogɸenous timeserài̖eƸs:W\n     \n\nό\x08\n==ǫē\x82=Ɠ===e=====Ƨ=×= ̵ ==ʕ======¼===    ======ɽ===\x85=q=δ=Ȇ===Ϣ    =æ==============ŧ\nΕ͜    timestamp Ĩ        \' seºgmen˨t3ť    ǏŲ ɛͲ̏     r̟Ȇe)Ǯgresăϊ̬sΘor_1            rǤϼe gr̝essoɓ̒ʏr_2\n=ƨ====Ĥ͚========Ú    ===Ƿ==ȕ==Ȑ\u0383==̩ˇƺ==    =====ª=====aʌΘ===== ș ̄====ǔ===¶========\n \n     \n2̎020-01-01 Ĕ    ƴ    segmenǾͳt_1        ϳ     ̺    ƙ 11        ƒ ŵ    Ġ \x8b˶ ʦ        n ϱ òʍ12\n2ʀ020-01˚-0ʱ2 ªœ Ū \x85    sègm͐heXÈnt_1ŧ                    ɋɄʬ22                     Ã        13\n2020-01-ĵ̺0ʉȑ3O        ú segm̶ent"_1         Ȣ Ʃ    ɼ Χ 3əȹ1̹ ʻ ΄                Ï    ϖ     g14̀\n20¼»20-01-0(4 ʊ͐¨ ǥĢ ɋ    segment_ϓ1ϧξ        ϗǓ     Ȇ     4Ƭï2    ¯ ĸ    ;    ɺ     ͗        ̶ 15\n...\n˕202È0-ɓ02-10ɓ H    ŋ    segment_2        \xa0        ϓǜ 10Ό1     ƭ    Ɇ     \\             61Ɣ̨\nɍ2020-0µ2ʰ-11     ɉ \x95 segment_2 ɽĤ        ˍǖ˟£ñƚ ʐʙ     ȼ20̣5    ^ «        Ȼ ̟         ŗ    5ʫ4\n=============    =ĥ¶=ˊϐ====ê=====    ǵ======ë===Ą\x91=ĔϦ==Ŧ=== 2 ===============')), Assign(targets=[Name(id='pipeline_configs', ctx=Store())], value=Call(func=Attribute(value=Name(id='OmegaConf', ctx=Load()), attr='to_object', ctx=Load()), args=[Call(func=Attribute(value=Name(id='OmegaConf', ctx=Load()), attr='load', ctx=Load()), args=[Name(id='config_path', ctx=Load())], keywords=[])], keywords=[])), Assign(targets=[Name(id='backtest_configs', ctx=Store())], value=Call(func=Attribute(value=Name(id='OmegaConf', ctx=Load()), attr='to_object', ctx=Load()), args=[Call(func=Attribute(value=Name(id='OmegaConf', ctx=Load()), attr='load', ctx=Load()), args=[Name(id='backtest_config_path', ctx=Load())], keywords=[])], keywords=[])), Assign(targets=[Name(id='df_timeseries', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='read_csv', ctx=Load()), args=[Name(id='target_path', ctx=Load())], keywords=[keyword(arg='parse_dates', value=List(elts=[Constant(value='timestamp')], ctx=Load()))])), Assign(targets=[Name(id='df_timeseries', ctx=Store())], value=Call(func=Attribute(value=Name(id='TSDataset', ctx=Load()), attr='to_dataset', ctx=Load()), args=[Name(id='df_timeseries', ctx=Load())], keywords=[])), Assign(targets=[Name(id='df_exog', ctx=Store())], value=Constant(value=None)), AnnAssign(target=Name(id='k_f', ctx=Store()), annotation=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Subscript(value=Name(id='Literal', ctx=Load()), slice=Constant(value='all'), ctx=Load()), Subscript(value=Name(id='Sequence', ctx=Load()), slice=Name(id='Any', ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load()), value=Tuple(elts=[], ctx=Load()), simple=1), If(test=Name(id='exog_path', ctx=Load()), body=[Assign(targets=[Name(id='df_exog', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='read_csv', ctx=Load()), args=[Name(id='exog_path', ctx=Load())], keywords=[keyword(arg='parse_dates', value=List(elts=[Constant(value='timestamp')], ctx=Load()))])), Assign(targets=[Name(id='df_exog', ctx=Store())], value=Call(func=Attribute(value=Name(id='TSDataset', ctx=Load()), attr='to_dataset', ctx=Load()), args=[Name(id='df_exog', ctx=Load())], keywords=[])), Assign(targets=[Name(id='k_f', ctx=Store())], value=IfExp(test=UnaryOp(op=Not(), operand=Name(id='known_future', ctx=Load())), body=Constant(value='all'), orelse=Name(id='known_future', ctx=Load())))], orelse=[]), Assign(targets=[Name(id='tsdataset', ctx=Store())], value=Call(func=Name(id='TSDataset', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='df_timeseries', ctx=Load())), keyword(arg='freq', value=Name(id='freq', ctx=Load())), keyword(arg='df_exog', value=Name(id='df_exog', ctx=Load())), keyword(arg='known_future', value=Name(id='k_f', ctx=Load()))])), AnnAssign(target=Name(id='pipeline', ctx=Store()), annotation=Name(id='Pipeline', ctx=Load()), value=Call(func=Attribute(value=Name(id='hydra_slayer', ctx=Load()), attr='get_from_params', ctx=Load()), args=[], keywords=[keyword(value=Name(id='pipeline_configs', ctx=Load()))]), simple=1), AnnAssign(target=Name(id='backtest_configs_hydra_slayer', ctx=Store()), annotation=Subscript(value=Name(id='Dict', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Name(id='Any', ctx=Load())], ctx=Load()), ctx=Load()), value=Call(func=Attribute(value=Name(id='hydra_slayer', ctx=Load()), attr='get_from_params', ctx=Load()), args=[], keywords=[keyword(value=Name(id='backtest_configs', ctx=Load()))]), simple=1), Assign(targets=[Tuple(elts=[Name(id='metrics', ctx=Store()), Name(id='forecast', ctx=Store()), Name(id='inforQSYS', ctx=Store())], ctx=Store())], value=Call(func=Attribute(value=Name(id='pipeline', ctx=Load()), attr='backtest', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='tsdataset', ctx=Load())), keyword(value=Name(id='backtest_configs_hydra_slayer', ctx=Load()))])), Expr(value=Call(func=Attribute(value=Name(id='metrics', ctx=Load()), attr='to_csv', ctx=Load()), args=[BinOp(left=Name(id='output_pat_h', ctx=Load()), op=Div(), right=Constant(value='metrics.csv'))], keywords=[keyword(arg='index', value=Constant(value=False))])), Expr(value=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='TSDataset', ctx=Load()), attr='to_flatten', ctx=Load()), args=[Name(id='forecast', ctx=Load())], keywords=[]), attr='to_csv', ctx=Load()), args=[BinOp(left=Name(id='output_pat_h', ctx=Load()), op=Div(), right=Constant(value='forecast.csv'))], keywords=[keyword(arg='index', value=Constant(value=False))])), Expr(value=Call(func=Attribute(value=Name(id='inforQSYS', ctx=Load()), attr='to_csv', ctx=Load()), args=[BinOp(left=Name(id='output_pat_h', ctx=Load()), op=Div(), right=Constant(value='info.csv'))], keywords=[keyword(arg='index', value=Constant(value=False))]))], decorator_list=[]), If(test=Compare(left=Name(id='__name__', ctx=Load()), ops=[Eq()], comparators=[Constant(value='__main__')]), body=[Expr(value=Call(func=Attribute(value=Name(id='typer', ctx=Load()), attr='run', ctx=Load()), args=[Name(id='backtest', ctx=Load())], keywords=[]))], orelse=[])], type_ignores=[])