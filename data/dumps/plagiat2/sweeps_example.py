Module(body=[Import(names=[alias(name='random')]), ImportFrom(module='typing', names=[alias(name='Optional')], level=0), ImportFrom(module='omegaconf', names=[alias(name='OmegaConf')], level=0), Import(names=[alias(name='pandas', asname='pd')]), Import(names=[alias(name='numpy', asname='np')]), ImportFrom(module='etna.datasets', names=[alias(name='TSDataset')], level=0), ImportFrom(module='omegaconf', names=[alias(name='DictConfig')], level=0), Import(names=[alias(name='hydra')]), Import(names=[alias(name='hydra_slayer')]), ImportFrom(module='pathlib', names=[alias(name='Path')], level=0), ImportFrom(module='etna.loggers', names=[alias(name='WandbLogger')], level=0), ImportFrom(module='etna.loggers', names=[alias(name='tslogger')], level=0), ImportFrom(module='etna.pipeline', names=[alias(name='Pipeline')], level=0), Expr(value=Call(func=Attribute(value=Name(id='OmegaConf', ctx=Load()), attr='register_new_resolver', ctx=Load()), args=[Constant(value='range'), Lambda(args=arguments(posonlyargs=[], args=[arg(arg='x'), arg(arg='Y')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Name(id='list', ctx=Load()), args=[Call(func=Name(id='range', ctx=Load()), args=[Name(id='x', ctx=Load()), Name(id='Y', ctx=Load())], keywords=[])], keywords=[]))], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='OmegaConf', ctx=Load()), attr='register_new_resolver', ctx=Load()), args=[Constant(value='sum'), Lambda(args=arguments(posonlyargs=[], args=[arg(arg='x'), arg(arg='Y')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=BinOp(left=Name(id='x', ctx=Load()), op=Add(), right=Name(id='Y', ctx=Load())))], keywords=[])), Assign(targets=[Name(id='FILE_PATH', ctx=Store())], value=Call(func=Name(id='Path', ctx=Load()), args=[Name(id='__file__', ctx=Load())], keywords=[])), FunctionDef(name='set_seed', args=arguments(posonlyargs=[], args=[arg(arg='se', annotation=Name(id='i', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=42)]), body=[Expr(value=Call(func=Attribute(value=Name(id='random', ctx=Load()), attr='seed', ctx=Load()), args=[Name(id='se', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='random', ctx=Load()), attr='seed', ctx=Load()), args=[Name(id='se', ctx=Load())], keywords=[]))], decorator_list=[]), FunctionDef(name='init_logger', args=arguments(posonlyargs=[], args=[arg(arg='con', annotation=Name(id='DICT', ctx=Load())), arg(arg='pro', annotation=Name(id='s', ctx=Load())), arg(arg='ta_gs', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='list', ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value='wandb-sweeps'), List(elts=[Constant(value='test'), Constant(value='sweeps')], ctx=Load())]), body=[Assign(targets=[Attribute(value=Name(id='tslogger', ctx=Load()), attr='loggers', ctx=Store())], value=List(elts=[], ctx=Load())), Assign(targets=[Name(id='wblogger', ctx=Store())], value=Call(func=Name(id='WandbLogger', ctx=Load()), args=[], keywords=[keyword(arg='project', value=Name(id='pro', ctx=Load())), keyword(arg='tags', value=Name(id='ta_gs', ctx=Load())), keyword(arg='config', value=Name(id='con', ctx=Load()))])), Expr(value=Call(func=Attribute(value=Name(id='tslogger', ctx=Load()), attr='add', ctx=Load()), args=[Name(id='wblogger', ctx=Load())], keywords=[]))], decorator_list=[]), FunctionDef(name='dataloader', args=arguments(posonlyargs=[], args=[arg(arg='file_path', annotation=Name(id='Path', ctx=Load())), arg(arg='freq', annotation=Name(id='s', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='\u0381̽@  Ăîʧģ Ϸ ọ̄8\x82ή  ς Ǝ Ɛ    ȏ   k   ¬  ')), Assign(targets=[Name(id='dfOBza', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='read_csv', ctx=Load()), args=[Name(id='file_path', ctx=Load())], keywords=[])), Assign(targets=[Name(id='dfOBza', ctx=Store())], value=Call(func=Attribute(value=Name(id='TSDataset', ctx=Load()), attr='to_dataset', ctx=Load()), args=[Name(id='dfOBza', ctx=Load())], keywords=[])), Assign(targets=[Name(id='t', ctx=Store())], value=Call(func=Name(id='TSDataset', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='dfOBza', ctx=Load())), keyword(arg='freq', value=Name(id='freq', ctx=Load()))])), Return(value=Name(id='t', ctx=Load()))], decorator_list=[], returns=Name(id='TSDataset', ctx=Load())), FunctionDef(name='objecti', args=arguments(posonlyargs=[], args=[arg(arg='cfg', annotation=Name(id='DictConfig', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value=' Rǩ̠  χǉ  ')), Assign(targets=[Name(id='con', ctx=Store())], value=Call(func=Attribute(value=Name(id='OmegaConf', ctx=Load()), attr='to_container', ctx=Load()), args=[Name(id='cfg', ctx=Load())], keywords=[keyword(arg='resolve', value=Constant(value=True))])), Expr(value=Call(func=Name(id='set_seed', ctx=Load()), args=[Attribute(value=Name(id='cfg', ctx=Load()), attr='seed', ctx=Load())], keywords=[])), Assign(targets=[Name(id='t', ctx=Store())], value=Call(func=Name(id='dataloader', ctx=Load()), args=[], keywords=[keyword(arg='file_path', value=Attribute(value=Attribute(value=Name(id='cfg', ctx=Load()), attr='dataset', ctx=Load()), attr='file_path', ctx=Load())), keyword(arg='freq', value=Attribute(value=Attribute(value=Name(id='cfg', ctx=Load()), attr='dataset', ctx=Load()), attr='freq', ctx=Load()))])), AnnAssign(target=Name(id='pipeline', ctx=Store()), annotation=Name(id='Pipeline', ctx=Load()), value=Call(func=Attribute(value=Name(id='hydra_slayer', ctx=Load()), attr='get_from_params', ctx=Load()), args=[], keywords=[keyword(value=Subscript(value=Name(id='con', ctx=Load()), slice=Constant(value='pipeline'), ctx=Load()))]), simple=1), Assign(targets=[Name(id='backtest_paramsysKV', ctx=Store())], value=Call(func=Attribute(value=Name(id='hydra_slayer', ctx=Load()), attr='get_from_params', ctx=Load()), args=[], keywords=[keyword(value=Subscript(value=Name(id='con', ctx=Load()), slice=Constant(value='backtest'), ctx=Load()))])), Expr(value=Call(func=Name(id='init_logger', ctx=Load()), args=[Call(func=Attribute(value=Name(id='pipeline', ctx=Load()), attr='to_dict', ctx=Load()), args=[], keywords=[])], keywords=[])), Assign(targets=[Tuple(elts=[Name(id='_', ctx=Store()), Name(id='_', ctx=Store()), Name(id='_', ctx=Store())], ctx=Store())], value=Call(func=Attribute(value=Name(id='pipeline', ctx=Load()), attr='backtest', ctx=Load()), args=[Name(id='t', ctx=Load())], keywords=[keyword(value=Name(id='backtest_paramsysKV', ctx=Load()))]))], decorator_list=[Call(func=Attribute(value=Name(id='hydra', ctx=Load()), attr='main', ctx=Load()), args=[], keywords=[keyword(arg='config_name', value=Constant(value='config.yaml'))])]), If(test=Compare(left=Name(id='__name__', ctx=Load()), ops=[Eq()], comparators=[Constant(value='__main__')]), body=[Expr(value=Call(func=Name(id='objecti', ctx=Load()), args=[], keywords=[]))], orelse=[])], type_ignores=[])