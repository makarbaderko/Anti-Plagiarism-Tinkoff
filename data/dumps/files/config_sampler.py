Module(body=[ImportFrom(module='typing', names=[alias(name='List')], level=0), ImportFrom(module='typing', names=[alias(name='Optional')], level=0), ImportFrom(module='typing', names=[alias(name='Set')], level=0), Import(names=[alias(name='numpy', asname='np')]), ImportFrom(module='optuna.samplers', names=[alias(name='BaseSampler')], level=0), ImportFrom(module='optuna.study', names=[alias(name='Study')], level=0), ImportFrom(module='optuna.trial', names=[alias(name='FrozenTrial')], level=0), ImportFrom(module='optuna.trial', names=[alias(name='TrialState')], level=0), ImportFrom(module='etna.auto.utils', names=[alias(name='config_hash')], level=0), ImportFrom(module='etna.auto.utils', names=[alias(name='retry')], level=0), ClassDef(name='ConfigSampler', bases=[Name(id='BaseSampler', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='Optuna based sampler for greedy search over different configurations.')), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='configs', annotation=Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='dict', ctx=Load()), ctx=Load())), arg(arg='random_generator', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='random', ctx=Load()), attr='Generator', ctx=Load()), ctx=Load())), arg(arg='retries', annotation=Name(id='int', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=None), Constant(value=10)]), body=[Expr(value=Constant(value='Init Config sampler.\n\n        Parameters\n        ----------\n        configs:\n            pool of configs to sample from\n        random_generator:\n            numpy generator to get reproducible samples\n        retries:\n            number of retries to get new sample from storage. It could be useful if storage is not reliable.\n        ')), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='configs', ctx=Store())], value=Name(id='configs', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='configs_hash', ctx=Store())], value=DictComp(key=Call(func=Name(id='config_hash', ctx=Load()), args=[], keywords=[keyword(arg='config', value=Name(id='config', ctx=Load()))]), value=Name(id='config', ctx=Load()), generators=[comprehension(target=Name(id='config', ctx=Store()), iter=Attribute(value=Name(id='self', ctx=Load()), attr='configs', ctx=Load()), ifs=[], is_async=0)])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_rng', ctx=Store())], value=Name(id='random_generator', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='retries', ctx=Store())], value=Name(id='retries', ctx=Load()))], decorator_list=[]), FunctionDef(name='sample_independent', args=arguments(posonlyargs=[], args=[arg(arg='self')], vararg=arg(arg='args'), kwonlyargs=[], kw_defaults=[], kwarg=arg(arg='kwargs'), defaults=[]), body=[Expr(value=Constant(value='Sample independent. Not used.')), Return(value=Dict(keys=[], values=[]))], decorator_list=[]), FunctionDef(name='infer_relative_search_space', args=arguments(posonlyargs=[], args=[arg(arg='self')], vararg=arg(arg='args'), kwonlyargs=[], kw_defaults=[], kwarg=arg(arg='kwargs'), defaults=[]), body=[Expr(value=Constant(value='Infer relative search space. Not used.')), Return(value=Dict(keys=[], values=[]))], decorator_list=[]), FunctionDef(name='sample_relative', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='study', annotation=Name(id='Study', ctx=Load())), arg(arg='trial', annotation=Name(id='FrozenTrial', ctx=Load()))], vararg=arg(arg='args'), kwonlyargs=[], kw_defaults=[], kwarg=arg(arg='kwargs'), defaults=[]), body=[Expr(value=Constant(value='Sample configuration to test.\n\n        Parameters\n        ----------\n        study:\n            current optuna study\n        trial:\n            optuna trial to use\n\n        Return\n        ------\n        :\n            sampled configuration to run objective on\n        ')), Assign(targets=[Name(id='trials_to_sample', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_get_unfinished_hashes', ctx=Load()), args=[], keywords=[keyword(arg='study', value=Name(id='study', ctx=Load())), keyword(arg='current_trial', value=Name(id='trial', ctx=Load()))])), If(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Name(id='trials_to_sample', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Constant(value=0)]), body=[Assign(targets=[Name(id='_to_sample', ctx=Store())], value=Call(func=Name(id='list', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='configs_hash', ctx=Load())], keywords=[])), Assign(targets=[Name(id='idx', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='rng', ctx=Load()), attr='choice', ctx=Load()), args=[Call(func=Name(id='len', ctx=Load()), args=[Name(id='_to_sample', ctx=Load())], keywords=[])], keywords=[])), Assign(targets=[Name(id='hash_to_sample', ctx=Store())], value=Subscript(value=Name(id='_to_sample', ctx=Load()), slice=Name(id='idx', ctx=Load()), ctx=Load()))], orelse=[Assign(targets=[Name(id='_trials_to_sample', ctx=Store())], value=Call(func=Name(id='list', ctx=Load()), args=[Name(id='trials_to_sample', ctx=Load())], keywords=[])), Assign(targets=[Name(id='idx', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='rng', ctx=Load()), attr='choice', ctx=Load()), args=[Call(func=Name(id='len', ctx=Load()), args=[Name(id='_trials_to_sample', ctx=Load())], keywords=[])], keywords=[])), Assign(targets=[Name(id='hash_to_sample', ctx=Store())], value=Subscript(value=Name(id='_trials_to_sample', ctx=Load()), slice=Name(id='idx', ctx=Load()), ctx=Load()))]), Assign(targets=[Name(id='map_to_objective', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='configs_hash', ctx=Load()), slice=Name(id='hash_to_sample', ctx=Load()), ctx=Load())), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='study', ctx=Load()), attr='_storage', ctx=Load()), attr='set_trial_user_attr', ctx=Load()), args=[Attribute(value=Name(id='trial', ctx=Load()), attr='_trial_id', ctx=Load()), Constant(value='hash'), Name(id='hash_to_sample', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='study', ctx=Load()), attr='_storage', ctx=Load()), attr='set_trial_user_attr', ctx=Load()), args=[Attribute(value=Name(id='trial', ctx=Load()), attr='_trial_id', ctx=Load()), Constant(value='pipeline'), Name(id='map_to_objective', ctx=Load())], keywords=[])), Return(value=Name(id='map_to_objective', ctx=Load()))], decorator_list=[], returns=Name(id='dict', ctx=Load())), FunctionDef(name='after_trial', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='study', annotation=Name(id='Study', ctx=Load())), arg(arg='trial', annotation=Name(id='FrozenTrial', ctx=Load()))], vararg=arg(arg='args'), kwonlyargs=[], kw_defaults=[], kwarg=arg(arg='kwargs'), defaults=[]), body=[Expr(value=Constant(value='Stop study if all configs have been tested.\n\n        Parameters\n        ----------\n        study:\n            current optuna study\n        ')), Assign(targets=[Name(id='unfinished_hashes', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_get_unfinished_hashes', ctx=Load()), args=[], keywords=[keyword(arg='study', value=Name(id='study', ctx=Load())), keyword(arg='current_trial', value=Name(id='trial', ctx=Load()))])), If(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Name(id='unfinished_hashes', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Constant(value=0)]), body=[Expr(value=Call(func=Attribute(value=Name(id='study', ctx=Load()), attr='stop', ctx=Load()), args=[], keywords=[]))], orelse=[]), If(test=BoolOp(op=And(), values=[Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Name(id='unfinished_hashes', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Constant(value=1)]), Compare(left=Subscript(value=Call(func=Name(id='list', ctx=Load()), args=[Name(id='unfinished_hashes', ctx=Load())], keywords=[]), slice=Constant(value=0), ctx=Load()), ops=[Eq()], comparators=[Subscript(value=Attribute(value=Name(id='trial', ctx=Load()), attr='user_attrs', ctx=Load()), slice=Constant(value='hash'), ctx=Load())])]), body=[Expr(value=Call(func=Attribute(value=Name(id='study', ctx=Load()), attr='stop', ctx=Load()), args=[], keywords=[]))], orelse=[])], decorator_list=[], returns=Constant(value=None)), FunctionDef(name='_get_unfinished_hashes', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='study', annotation=Name(id='Study', ctx=Load())), arg(arg='current_trial', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='FrozenTrial', ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=None)]), body=[Expr(value=Constant(value='Get unfinished config hashes.\n\n        Parameters\n        ----------\n        study:\n            current optuna study\n\n        Returns\n        -------\n        :\n            hashes to run\n        ')), Assign(targets=[Name(id='trials', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='study', ctx=Load()), attr='_storage', ctx=Load()), attr='get_all_trials', ctx=Load()), args=[Attribute(value=Name(id='study', ctx=Load()), attr='_study_id', ctx=Load())], keywords=[keyword(arg='deepcopy', value=Constant(value=False))])), If(test=Compare(left=Name(id='current_trial', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), body=[Assign(targets=[Name(id='trials', ctx=Store())], value=ListComp(elt=Name(id='trial', ctx=Load()), generators=[comprehension(target=Name(id='trial', ctx=Store()), iter=Name(id='trials', ctx=Load()), ifs=[Compare(left=Attribute(value=Name(id='trial', ctx=Load()), attr='_trial_id', ctx=Load()), ops=[NotEq()], comparators=[Attribute(value=Name(id='current_trial', ctx=Load()), attr='_trial_id', ctx=Load())])], is_async=0)]))], orelse=[]), Assign(targets=[Name(id='finished_trials_hash', ctx=Store())], value=List(elts=[], ctx=Load())), Assign(targets=[Name(id='running_trials_hash', ctx=Store())], value=List(elts=[], ctx=Load())), For(target=Name(id='t', ctx=Store()), iter=Name(id='trials', ctx=Load()), body=[If(test=Call(func=Attribute(value=Attribute(value=Name(id='t', ctx=Load()), attr='state', ctx=Load()), attr='is_finished', ctx=Load()), args=[], keywords=[]), body=[Expr(value=Call(func=Attribute(value=Name(id='finished_trials_hash', ctx=Load()), attr='append', ctx=Load()), args=[Subscript(value=Attribute(value=Name(id='t', ctx=Load()), attr='user_attrs', ctx=Load()), slice=Constant(value='hash'), ctx=Load())], keywords=[]))], orelse=[If(test=Compare(left=Attribute(value=Name(id='t', ctx=Load()), attr='state', ctx=Load()), ops=[Eq()], comparators=[Attribute(value=Name(id='TrialState', ctx=Load()), attr='RUNNING', ctx=Load())]), body=[FunctionDef(name='_closure', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=Subscript(value=Attribute(value=Call(func=Attribute(value=Attribute(value=Name(id='study', ctx=Load()), attr='_storage', ctx=Load()), attr='get_trial', ctx=Load()), args=[Attribute(value=Name(id='t', ctx=Load()), attr='_trial_id', ctx=Load())], keywords=[]), attr='user_attrs', ctx=Load()), slice=Constant(value='hash'), ctx=Load()))], decorator_list=[]), Assign(targets=[Name(id='hash_to_add', ctx=Store())], value=Call(func=Name(id='retry', ctx=Load()), args=[Name(id='_closure', ctx=Load())], keywords=[keyword(arg='max_retries', value=Attribute(value=Name(id='self', ctx=Load()), attr='retries', ctx=Load()))])), Expr(value=Call(func=Attribute(value=Name(id='running_trials_hash', ctx=Load()), attr='append', ctx=Load()), args=[Name(id='hash_to_add', ctx=Load())], keywords=[]))], orelse=[Pass()])])], orelse=[]), Return(value=BinOp(left=BinOp(left=Call(func=Name(id='set', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='configs_hash', ctx=Load())], keywords=[]), op=Sub(), right=Call(func=Name(id='set', ctx=Load()), args=[Name(id='finished_trials_hash', ctx=Load())], keywords=[])), op=Sub(), right=Call(func=Name(id='set', ctx=Load()), args=[Name(id='running_trials_hash', ctx=Load())], keywords=[])))], decorator_list=[], returns=Subscript(value=Name(id='Set', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load())), FunctionDef(name='rng', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[If(test=Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='_rng', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_rng', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='random', ctx=Load()), attr='default_rng', ctx=Load()), args=[], keywords=[]))], orelse=[]), Return(value=Attribute(value=Name(id='self', ctx=Load()), attr='_rng', ctx=Load()))], decorator_list=[Name(id='property', ctx=Load())]), FunctionDef(name='get_config_by_hash', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='hash', annotation=Name(id='str', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Get config by hash.\n\n        Parameters\n        ----------\n        hash:\n            hash to get config for\n        ')), Return(value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='configs_hash', ctx=Load()), slice=Name(id='hash', ctx=Load()), ctx=Load()))], decorator_list=[])], decorator_list=[])], type_ignores=[])