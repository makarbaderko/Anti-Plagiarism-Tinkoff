Module(body=[ImportFrom(module='setuptools', names=[alias(name='setup'), alias(name='find_namespace_packages')], level=0), Expr(value=Call(func=Name(id='setup', ctx=Load()), args=[], keywords=[keyword(arg='version', value=Constant(value='0.1.0')), keyword(arg='name', value=Constant(value='probabilistic_embeddings')), keyword(arg='long_description', value=Constant(value='Experiments with MDN for metric learning.')), keyword(arg='url', value=Constant(value='https://github.com/tinkoff-ai/probabilistic-embeddings')), keyword(arg='author', value=Constant(value='Ivan Karpukhin and Stanislav Dereka')), keyword(arg='author_email', value=Constant(value='karpuhini@yandex.ru')), keyword(arg='packages', value=Call(func=Name(id='find_namespace_packages', ctx=Load()), args=[], keywords=[keyword(arg='where', value=Constant(value='src'))])), keyword(arg='package_dir', value=Dict(keys=[Constant(value='')], values=[Constant(value='src')])), keyword(arg='install_requires', value=List(elts=[Constant(value='catalyst==21.9'), Constant(value='faiss-cpu==1.7.0'), Constant(value='jpeg4py==0.1.4'), Constant(value='mxnet==1.8.0.post0'), Constant(value='numpy==1.19.5'), Constant(value='optuna==2.10.0'), Constant(value='pretrainedmodels==0.7.4'), Constant(value='scikit-image==0.17.2'), Constant(value='scikit-learn==0.24.2'), Constant(value='scipy==1.5.4'), Constant(value='torch==1.10.1'), Constant(value='torchvision==0.11.2'), Constant(value='Pillow==8.3.1'), Constant(value='PyYAML==5.4.1'), Constant(value='gitpython'), Constant(value='wandb')], ctx=Load()))]))], type_ignores=[])