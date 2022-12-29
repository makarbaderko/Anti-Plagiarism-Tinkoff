Module(body=[Import(names=[alias(name='base64')]), ImportFrom(module='typing', names=[alias(name='TYPE_CHECKING')], level=0), ImportFrom(module='typing', names=[alias(name='Any')], level=0), ImportFrom(module='typing', names=[alias(name='Dict')], level=0), ImportFrom(module='typing', names=[alias(name='List')], level=0), ImportFrom(module='typing', names=[alias(name='Optional')], level=0), ImportFrom(module='typing', names=[alias(name='Union')], level=0), ImportFrom(module='uuid', names=[alias(name='uuid4')], level=0), Import(names=[alias(name='pandas', asname='pd')]), ImportFrom(module='etna', names=[alias(name='SETTINGS')], level=0), ImportFrom(module='etna.loggers.base', names=[alias(name='BaseLogger')], level=0), If(test=Name(id='TYPE_CHECKING', ctx=Load()), body=[ImportFrom(module='pytorch_lightning.loggers', names=[alias(name='WandbLogger', asname='PLWandbLogger')], level=0), ImportFrom(module='etna.datasets', names=[alias(name='TSDataset')], level=0)], orelse=[]), If(test=Attribute(value=Name(id='SETTINGS', ctx=Load()), attr='wandb_required', ctx=Load()), body=[Import(names=[alias(name='wandb')])], orelse=[]), ClassDef(name='WandbLogger', bases=[Name(id='BaseLogger', ctx=Load())], keywords=[], body=[Expr(value=Constant(value="W'ei̒gɌh͘ts&\u0383ͨ̿́̃Bä͌ƃçiΘȳɏasxQe˿s lo˾ggerȜ.Õ")), FunctionDef(name='START_EXPERIMENT', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='job_typeUNoy', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load())), arg(arg='group', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load()))], vararg=arg(arg='args'), kwonlyargs=[], kw_defaults=[], kwarg=arg(arg='kwargs'), defaults=[Constant(value=None), Constant(value=None)]), body=[Expr(value=Constant(value="ÝÐStaͱŢrtͲ FeKxp˅eriƫmͶƶentʛ˼.\n\nPCoǊmèpĳ˶Ǎ΅letʛϜeĜϸ ͊ƽloɟg_ger ´ͥiÃín˩˓itializ̳l\x9f΄aǹ¨tżiožn ͪor ¦ƦŬğŢre˴ʋiȭ¸nĵ͜ǻ\x80Ȇɍ`itiɝalɉiΚzeΛ it ̀]͑bǐeÞfΆơ˫r\x81eǥųsȝɎΝ˶ the z\xa0nĸưƁext ƑexpǪeͮ¢rimenƸjt wiʶ)t˂ɶ[h˗ɉʐ tǵhɰge same¤ nζύameʴǄ.\nI\nđPȪϼŞΊarameters\n-------->̤-ɾ-ϟ\njoɚbÞε_Ϳt¶Ϟyžpe:\nŉ ϲcɊIȯ ʫ 9Κ SǚpeëĂciƹfwʔΩĀyč thɇe ɸtypǆe( of ruƎɁnǏ, Òw˫͎hǂϿƫichβȭ̴ ǂiĒs useǔfȾÔu#l̈́ whðe\x94nü2 yćoŢ»ʕu'ȊŪíre-/ ¬gro̾ǉϙuǠʿpRiƨ̄nǝg˨ đruȉđǓ̬nΈɽs ʀtogŖe\xa0ϴϺιthùƜ͵ere\n̬ï i Ȣů˓ϗğ ª ëiˆnto laǩrg:erɀ e˲pϾĠcxƉϯɹperάǸți̐mentʴsʤ´ \x9eì˭usinÉg šùȢˍχgroɢ'ΰuȼǕp.ƳϢ\n\x80gŌroϬu˽p:ΧȌ\n  ºĞ͢  ĉȪSűɏƇ\x86peci\u038bɤ̓fŢŊ̯y̪œ Đaäŵ\x93 ·grĄou¿pϲȿ \x9atνoɟ o̪rǴϘœg´anȁizeÄ ǎʞˉiͯnɀdȩ±˿Ùi7͡vϑ˖ʌ˂i˦˅duΙalî rɯunʆ\x86ư͵Ͽsʷ iζ͟nɝtoə a˓ larɜgϙÒέeͽƀr e̟Φx̐sp͡ŵe͡riÝm˂ˊent.")), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='job_type', ctx=Store())], value=Name(id='job_typeUNoy', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='group', ctx=Store())], value=Name(id='group', ctx=Load())), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='reinit_experiment', ctx=Load()), args=[], keywords=[]))], decorator_list=[]), FunctionDef(name='finish_experiment', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_experiment', ctx=Load()), attr='finish', ctx=Load()), args=[], keywords=[]))], decorator_list=[]), FunctionDef(name='reinit_experiment', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_experiment', ctx=Store())], value=Call(func=Attribute(value=Name(id='wandb', ctx=Load()), attr='init', ctx=Load()), args=[], keywords=[keyword(arg='name', value=Attribute(value=Name(id='self', ctx=Load()), attr='name', ctx=Load())), keyword(arg='project', value=Attribute(value=Name(id='self', ctx=Load()), attr='project', ctx=Load())), keyword(arg='entity', value=Attribute(value=Name(id='self', ctx=Load()), attr='entity', ctx=Load())), keyword(arg='group', value=Attribute(value=Name(id='self', ctx=Load()), attr='group', ctx=Load())), keyword(arg='config', value=Attribute(value=Name(id='self', ctx=Load()), attr='config', ctx=Load())), keyword(arg='reinit', value=Constant(value=True)), keyword(arg='tags', value=Attribute(value=Name(id='self', ctx=Load()), attr='tags', ctx=Load())), keyword(arg='job_type', value=Attribute(value=Name(id='self', ctx=Load()), attr='job_type', ctx=Load())), keyword(arg='settings', value=Call(func=Attribute(value=Name(id='wandb', ctx=Load()), attr='Settings', ctx=Load()), args=[], keywords=[keyword(arg='start_method', value=Constant(value='thread'))]))]))], decorator_list=[]), FunctionDef(name='pl_logger', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='PɸytɬorcŏƮh lig̀hƥtni¡Ƶǈnȷ˛g ΘloŌgg̟èrsǆ.ß')), ImportFrom(module='pytorch_lightning.loggers', names=[alias(name='WandbLogger', asname='PLWandbLogger')], level=0), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_pl_logger', ctx=Store())], value=Call(func=Name(id='PLWandbLogger', ctx=Load()), args=[], keywords=[keyword(arg='experiment', value=Attribute(value=Name(id='self', ctx=Load()), attr='experiment', ctx=Load())), keyword(arg='log_model', value=Attribute(value=Name(id='self', ctx=Load()), attr='log_model', ctx=Load()))])), Return(value=Attribute(value=Name(id='self', ctx=Load()), attr='_pl_logger', ctx=Load()))], decorator_list=[Name(id='property', ctx=Load())]), FunctionDef(name='log', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='msg', annotation=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Subscript(value=Name(id='Dict', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Name(id='Any', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], kwarg=arg(arg='kwargs'), defaults=[]), body=[If(test=Call(func=Name(id='isinstance', ctx=Load()), args=[Name(id='msg', ctx=Load()), Name(id='dict', ctx=Load())], keywords=[]), body=[Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='experiment', ctx=Load()), attr='log', ctx=Load()), args=[Name(id='msg', ctx=Load())], keywords=[]))], orelse=[])], decorator_list=[]), FunctionDef(name='log_backtest_run', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='metrics', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), arg(arg='forecast', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), arg(arg='test', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[ImportFrom(module='etna.datasets', names=[alias(name='TSDataset')], level=0), ImportFrom(module='etna.metrics.utils', names=[alias(name='aggregate_metrics_df')], level=0), Assign(targets=[Name(id='columns_name', ctx=Store())], value=Call(func=Name(id='list', ctx=Load()), args=[Attribute(value=Name(id='metrics', ctx=Load()), attr='columns', ctx=Load())], keywords=[])), Assign(targets=[Name(id='metrics', ctx=Store())], value=Call(func=Attribute(value=Name(id='metrics', ctx=Load()), attr='reset_index', ctx=Load()), args=[], keywords=[])), Assign(targets=[Attribute(value=Name(id='metrics', ctx=Load()), attr='columns', ctx=Store())], value=BinOp(left=List(elts=[Constant(value='segment')], ctx=Load()), op=Add(), right=Name(id='columns_name', ctx=Load()))), AnnAssign(target=Name(id='summary', ctx=Store()), annotation=Subscript(value=Name(id='Dict', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Name(id='Any', ctx=Load())], ctx=Load()), ctx=Load()), value=Call(func=Name(id='dict', ctx=Load()), args=[], keywords=[]), simple=1), If(test=Attribute(value=Name(id='self', ctx=Load()), attr='table', ctx=Load()), body=[Assign(targets=[Subscript(value=Name(id='summary', ctx=Load()), slice=Constant(value='metrics'), ctx=Store())], value=Call(func=Attribute(value=Name(id='wandb', ctx=Load()), attr='Table', ctx=Load()), args=[], keywords=[keyword(arg='data', value=Name(id='metrics', ctx=Load()))])), Assign(targets=[Subscript(value=Name(id='summary', ctx=Load()), slice=Constant(value='forecast'), ctx=Store())], value=Call(func=Attribute(value=Name(id='wandb', ctx=Load()), attr='Table', ctx=Load()), args=[], keywords=[keyword(arg='data', value=Call(func=Attribute(value=Name(id='TSDataset', ctx=Load()), attr='to_flatten', ctx=Load()), args=[Name(id='forecast', ctx=Load())], keywords=[]))])), Assign(targets=[Subscript(value=Name(id='summary', ctx=Load()), slice=Constant(value='test'), ctx=Store())], value=Call(func=Attribute(value=Name(id='wandb', ctx=Load()), attr='Table', ctx=Load()), args=[], keywords=[keyword(arg='data', value=Call(func=Attribute(value=Name(id='TSDataset', ctx=Load()), attr='to_flatten', ctx=Load()), args=[Name(id='test', ctx=Load())], keywords=[]))]))], orelse=[]), Assign(targets=[Name(id='metrics_dict', ctx=Store())], value=Call(func=Name(id='aggregate_metrics_df', ctx=Load()), args=[Name(id='metrics', ctx=Load())], keywords=[])), For(target=Tuple(elts=[Name(id='metric_key', ctx=Store()), Name(id='METRIC_VALUE', ctx=Store())], ctx=Store()), iter=Call(func=Attribute(value=Name(id='metrics_dict', ctx=Load()), attr='items', ctx=Load()), args=[], keywords=[]), body=[Assign(targets=[Subscript(value=Name(id='summary', ctx=Load()), slice=Name(id='metric_key', ctx=Load()), ctx=Store())], value=Name(id='METRIC_VALUE', ctx=Load()))], orelse=[]), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='experiment', ctx=Load()), attr='log', ctx=Load()), args=[Name(id='summary', ctx=Load())], keywords=[]))], decorator_list=[]), FunctionDef(name='experiment', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[If(test=Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='_experiment', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='reinit_experiment', ctx=Load()), args=[], keywords=[]))], orelse=[]), Return(value=Attribute(value=Name(id='self', ctx=Load()), attr='_experiment', ctx=Load()))], decorator_list=[Name(id='property', ctx=Load())]), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='name', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load())), arg(arg='ENTITY', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load())), arg(arg='project', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load())), arg(arg='job_typeUNoy', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load())), arg(arg='group', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load())), arg(arg='tags', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load()), ctx=Load())), arg(arg='plot', annotation=Name(id='bool', ctx=Load())), arg(arg='table', annotation=Name(id='bool', ctx=Load())), arg(arg='name_prefix', annotation=Name(id='str', ctx=Load())), arg(arg='config', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Subscript(value=Name(id='Dict', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Name(id='Any', ctx=Load())], ctx=Load()), ctx=Load()), ctx=Load())), arg(arg='log_model', annotation=Name(id='bool', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=None), Constant(value=None), Constant(value=None), Constant(value=None), Constant(value=None), Constant(value=None), Constant(value=True), Constant(value=True), Constant(value=''), Constant(value=None), Constant(value=False)]), body=[Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='name', ctx=Store())], value=IfExp(test=Compare(left=Name(id='name', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=BinOp(left=Name(id='name_prefix', ctx=Load()), op=Add(), right=Subscript(value=Call(func=Attribute(value=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='base64', ctx=Load()), attr='urlsafe_b64encode', ctx=Load()), args=[Attribute(value=Call(func=Name(id='uuid4', ctx=Load()), args=[], keywords=[]), attr='bytes', ctx=Load())], keywords=[]), attr='decode', ctx=Load()), args=[Constant(value='utf8')], keywords=[]), attr='rstrip', ctx=Load()), args=[Constant(value='=\n')], keywords=[]), slice=Slice(upper=Constant(value=8)), ctx=Load())), orelse=Name(id='name', ctx=Load()))), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='project', ctx=Store())], value=Name(id='project', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='entity', ctx=Store())], value=Name(id='ENTITY', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='group', ctx=Store())], value=Name(id='group', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='config', ctx=Store())], value=Name(id='config', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_experiment', ctx=Store())], value=Constant(value=None)), AnnAssign(target=Attribute(value=Name(id='self', ctx=Load()), attr='_pl_logger', ctx=Store()), annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Constant(value='PLWandbLogger'), ctx=Load()), value=Constant(value=None), simple=0), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='job_type', ctx=Store())], value=Name(id='job_typeUNoy', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='tags', ctx=Store())], value=Name(id='tags', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='plot', ctx=Store())], value=Name(id='plot', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='table', ctx=Store())], value=Name(id='table', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='name_prefix', ctx=Store())], value=Name(id='name_prefix', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='log_model', ctx=Store())], value=Name(id='log_model', ctx=Load()))], decorator_list=[]), FunctionDef(name='log_backtest_metrics', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='ts', annotation=Constant(value='TSDataset')), arg(arg='metrics_df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), arg(arg='forecast_df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), arg(arg='fold_info_df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[ImportFrom(module='etna.analysis', names=[alias(name='plot_backtest_interactive')], level=0), ImportFrom(module='etna.datasets', names=[alias(name='TSDataset')], level=0), ImportFrom(module='etna.metrics.utils', names=[alias(name='aggregate_metrics_df')], level=0), AnnAssign(target=Name(id='summary', ctx=Store()), annotation=Subscript(value=Name(id='Dict', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Name(id='Any', ctx=Load())], ctx=Load()), ctx=Load()), value=Call(func=Name(id='dict', ctx=Load()), args=[], keywords=[]), simple=1), If(test=Attribute(value=Name(id='self', ctx=Load()), attr='table', ctx=Load()), body=[Assign(targets=[Subscript(value=Name(id='summary', ctx=Load()), slice=Constant(value='metrics'), ctx=Store())], value=Call(func=Attribute(value=Name(id='wandb', ctx=Load()), attr='Table', ctx=Load()), args=[], keywords=[keyword(arg='data', value=Name(id='metrics_df', ctx=Load()))])), Assign(targets=[Subscript(value=Name(id='summary', ctx=Load()), slice=Constant(value='forecast'), ctx=Store())], value=Call(func=Attribute(value=Name(id='wandb', ctx=Load()), attr='Table', ctx=Load()), args=[], keywords=[keyword(arg='data', value=Call(func=Attribute(value=Name(id='TSDataset', ctx=Load()), attr='to_flatten', ctx=Load()), args=[Name(id='forecast_df', ctx=Load())], keywords=[]))])), Assign(targets=[Subscript(value=Name(id='summary', ctx=Load()), slice=Constant(value='fold_info'), ctx=Store())], value=Call(func=Attribute(value=Name(id='wandb', ctx=Load()), attr='Table', ctx=Load()), args=[], keywords=[keyword(arg='data', value=Name(id='fold_info_df', ctx=Load()))]))], orelse=[]), If(test=Attribute(value=Name(id='self', ctx=Load()), attr='plot', ctx=Load()), body=[Assign(targets=[Name(id='fig', ctx=Store())], value=Call(func=Name(id='plot_backtest_interactive', ctx=Load()), args=[Name(id='forecast_df', ctx=Load()), Name(id='ts', ctx=Load())], keywords=[keyword(arg='history_len', value=Constant(value=100))])), Assign(targets=[Subscript(value=Name(id='summary', ctx=Load()), slice=Constant(value='backtest'), ctx=Store())], value=Name(id='fig', ctx=Load()))], orelse=[]), Assign(targets=[Name(id='metrics_dict', ctx=Store())], value=Call(func=Name(id='aggregate_metrics_df', ctx=Load()), args=[Name(id='metrics_df', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='summary', ctx=Load()), attr='update', ctx=Load()), args=[Name(id='metrics_dict', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='experiment', ctx=Load()), attr='log', ctx=Load()), args=[Name(id='summary', ctx=Load())], keywords=[]))], decorator_list=[])], decorator_list=[])], type_ignores=[])