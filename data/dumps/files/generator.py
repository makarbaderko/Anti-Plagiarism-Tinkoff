Module(body=[ImportFrom(module='enum', names=[alias(name='Enum')], level=0), ImportFrom(module='typing', names=[alias(name='List')], level=0), ImportFrom(module='hydra_slayer', names=[alias(name='get_from_params')], level=0), ImportFrom(module='etna.auto.pool.templates', names=[alias(name='DEFAULT')], level=0), ImportFrom(module='etna.auto.pool.utils', names=[alias(name='fill_template')], level=0), ImportFrom(module='etna.pipeline', names=[alias(name='Pipeline')], level=0), ClassDef(name='PoolGenerator', bases=[], keywords=[], body=[Expr(value=Constant(value='Generate a pool of pipelines from given config templates in hydra format.')), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='configs_template', annotation=Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='dict', ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value="\n        Initialize with a list of config templates in hydra format.\n\n        Parameters\n        ----------\n        configs_template:\n            list of template configs in hydra format\n\n        Notes\n        -----\n        Hydra configs templates:\n        ::\n            {\n                '_target_': 'etna.pipeline.Pipeline',\n                'horizon': '${__aux__.horizon}',\n                'model': {'_target_': 'etna.models.ProphetModel'}\n            }\n        Values to be interpolated should be in the form of ``${__aux__.key}``\n        ")), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='configs_template', ctx=Store())], value=Name(id='configs_template', ctx=Load()))], decorator_list=[]), FunctionDef(name='generate', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='horizon', annotation=Name(id='int', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='\n        Fill templates with args.\n\n        Parameters\n        ----------\n        horizon:\n            horizon to forecast\n        ')), AnnAssign(target=Name(id='filled_templates', ctx=Store()), annotation=Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='dict', ctx=Load()), ctx=Load()), value=ListComp(elt=Call(func=Name(id='fill_template', ctx=Load()), args=[Name(id='config', ctx=Load()), Dict(keys=[Constant(value='horizon')], values=[Name(id='horizon', ctx=Load())])], keywords=[]), generators=[comprehension(target=Name(id='config', ctx=Store()), iter=Attribute(value=Name(id='self', ctx=Load()), attr='configs_template', ctx=Load()), ifs=[], is_async=0)]), simple=1), Return(value=ListComp(elt=Call(func=Name(id='get_from_params', ctx=Load()), args=[], keywords=[keyword(value=Name(id='filled_template', ctx=Load()))]), generators=[comprehension(target=Name(id='filled_template', ctx=Store()), iter=Name(id='filled_templates', ctx=Load()), ifs=[], is_async=0)]))], decorator_list=[], returns=Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='Pipeline', ctx=Load()), ctx=Load()))], decorator_list=[]), ClassDef(name='Pool', bases=[Name(id='Enum', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='Predefined pools of pipelines.')), Assign(targets=[Name(id='default', ctx=Store())], value=Call(func=Name(id='PoolGenerator', ctx=Load()), args=[], keywords=[keyword(arg='configs_template', value=Name(id='DEFAULT', ctx=Load()))]))], decorator_list=[])], type_ignores=[])