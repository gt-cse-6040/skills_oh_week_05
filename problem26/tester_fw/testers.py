from .tester_6040 import *
from .test_utils import *       

class Tester_ex1(ExerciseTester):
    def __init__(self, key=b'sIRWMgIhwENImJyOel3HWJDMr0VbXzfbq-uwgd09VFs=',  path='resource/asnlib/publicdata/', prevent_mod=True, tc_path=None):
        super().__init__(prevent_mod, tc_path)
        import pickle
        from cryptography.fernet import Fernet
        fernet = Fernet(key)
        try:
            with open(path + 'tc_ex1.pkl', 'rb') as fin:
                self.cases = pickle.loads(fernet.decrypt(fin.read()))
        except FileNotFoundError:
            print('file not found - Tester_ex1 may not work as expected')

    def build_vars(self):
        ### begin build_vars_ex1
        ### define build_vars_helper(cases)
        def build_vars_helper(cases):
            from random import choice
            case = choice(cases)
            input_vars = {'lod': case['lod']}
            true_output_vars = {'keys': case['keys']}
            return input_vars, true_output_vars
        ### end build_vars_ex1
        self.input_vars, self.true_output_vars = build_vars_helper(self.cases)

    def run_func(self, func):
        ### begin run_func_ex1
        ### define run_func_helper(func, inputs)
        def run_func_helper(func, inputs):
            return {
                'keys': func(**inputs)
            }
        ### end run_func_ex1
        self.returned_output_vars = run_func_helper(func, self.input_vars)

    def check_type(self):
        ### begin check_type_ex1
        ### define check_type(outputs)
        def check_type_helper(outputs):
            t = type(outputs['keys'])
            assert t is set, f'The output is required to be a `set`. However, your solution returned a {t}.'
        ### end check_type_ex1
        check_type_helper(self.returned_output_vars)


    def check_matches(self):
        ### begin check_matches_ex1
        ### Define check_matches_helper(returned_outputs, true_outputs)
        def check_matches_helper(returned_outputs, true_outputs):
            from tester_fw.test_utils import compare_copies
            r, t = returned_outputs['keys'], true_outputs['keys']
            assert compare_copies(r, t), 'Your output does not match the solution. Please check the testing variables (input_vars, original_input_vars, returned_output_vars, true_output_vars) for debugging.'
        ### end check_matches_ex1
        check_matches_helper(self.returned_output_vars, self.true_output_vars)

class Tester_ex2(ExerciseTester):
    def __init__(self, key=b'sIRWMgIhwENImJyOel3HWJDMr0VbXzfbq-uwgd09VFs=',  path='resource/asnlib/publicdata/', prevent_mod=True, tc_path=None):
        super().__init__(prevent_mod, tc_path)
        import pickle
        from cryptography.fernet import Fernet
        fernet = Fernet(key)
        try:
            with open(path + 'tc_ex2.pkl', 'rb') as fin:
                self.cases = pickle.loads(fernet.decrypt(fin.read()))
        except FileNotFoundError:
            print('file not found - Tester_ex2 may not work as expected')

    def build_vars(self):
        ### begin build_vars_ex2
        ### define build_vars_helper(cases)
        def build_vars_helper(cases):
            from random import choice
            case = choice(cases)
            input_vars = {'lod': case['lod']}
            true_output_vars = {'basic_data': case['basic_data']}
            return input_vars, true_output_vars
        ### end build_vars_ex2
        self.input_vars, self.true_output_vars = build_vars_helper(self.cases)

    def run_func(self, func):
        ### begin run_func_ex2
        ### define run_func_helper(func, inputs)
        def run_func_helper(func, inputs):
            return {'basic_data': func(**inputs)}
        ### end run_func_ex2
        self.returned_output_vars = run_func_helper(func, self.input_vars)

    def check_type(self):
        ### begin check_type_ex2
        ### define check_type(outputs)
        def check_type_helper(outputs):
            from tester_fw.test_utils import compare_copies
            lod = outputs['basic_data']
            t = type(lod)
            assert t is list, f'The output must be an instance of `list`, type {t} was returned instead.'
            true_keys = {'description', 'list_of_ingredients', 'raw_nutrients', 'category'}
            for o in lod:
                assert isinstance(o, dict), f'each entry in `basic_data` must be a `dict`, type {type(o)} was returned instead'
                assert compare_copies(true_keys, set(o.keys())), 'Your output does not have the correct keys.'
                t = type(o['description'])
                assert t is str, f'description should be `str`, type {t} was returned instead.'
                t = type(o['category'])
                assert t is str, f'category should be `str`, type {t} was returned instead.'
                t = type(o['raw_nutrients'])
                assert isinstance(o, dict), f'raw_nutrients should be an instance of `dict`, type {t} was returned instead.'
                for k, v in o['raw_nutrients'].items():
                    t = type(k)
                    assert t is str, f'raw nutrient keys should be `str`, type {t} was returned instead.'
                    t = type(v)
                    assert t is float, f'raw nutrient values should be `float`, type {t} was returned instead.'
                t = type(o['list_of_ingredients'])
                assert t is list, f'list_of_ingredients should be `list`, type {t} was returned instead.'
                for v in o['list_of_ingredients']:
                    t = type(v)
                    assert t is str, f'individual ingredients should be `str`, type {t} was returned instead.'
        ### end check_type_ex2
        check_type_helper(self.returned_output_vars)


    def check_matches(self):
        ### begin check_matches_ex2
        ### Define check_matches_helper(returned_outputs, true_outputs)
        def check_matches_helper(returned_outputs, true_outputs):
            from tester_fw.test_utils import compare_copies
            assert compare_copies(returned_outputs['basic_data'], true_outputs['basic_data']), 'Your solution does not match the expected solution'
        ### end check_matches_ex2
        check_matches_helper(self.returned_output_vars, self.true_output_vars)

class Tester_ex3(ExerciseTester):
    def __init__(self, key=b'sIRWMgIhwENImJyOel3HWJDMr0VbXzfbq-uwgd09VFs=',  path='resource/asnlib/publicdata/', prevent_mod=True, tc_path=None):
        super().__init__(prevent_mod, tc_path)
        import pickle
        from cryptography.fernet import Fernet
        fernet = Fernet(key)
        try:
            with open(path + 'tc_ex3.pkl', 'rb') as fin:
                self.cases = pickle.loads(fernet.decrypt(fin.read()))
        except FileNotFoundError:
            print('file not found - Tester_ex3 may not work as expected')

    def build_vars(self):
        ### begin build_vars_ex3
        ### define build_vars_helper(cases)
        def build_vars_helper(cases):
            from random import choice
            case = choice(cases)
            input_vars = {'data': case['data']}
            true_output_vars = {'filtered': case['filtered']}
            return input_vars, true_output_vars
        ### end build_vars_ex3
        self.input_vars, self.true_output_vars = build_vars_helper(self.cases)

    def run_func(self, func):
        ### begin run_func_ex3
        ### define run_func_helper(func, inputs)
        def run_func_helper(func, inputs):
            return {'filtered': func(**inputs)}
        ### end run_func_ex3
        self.returned_output_vars = run_func_helper(func, self.input_vars)

    def check_type(self):
        ### begin check_type_ex3
        ### define check_type(outputs)
        def check_type_helper(outputs):
            filtered = outputs['filtered']
            t = type(filtered)
            assert t is list, f'Output must be a `list`, but type {t} was returned.'
            for d in filtered:
                assert isinstance(d, dict), f'Entries in output list must be `dict`, but {type(d)} was returned'
        ### end check_type_ex3
        check_type_helper(self.returned_output_vars)


    def check_matches(self):
        ### begin check_matches_ex3
        ### Define check_matches_helper(returned_outputs, true_outputs)
        def check_matches_helper(returned_outputs, true_outputs):
            from tester_fw.test_utils import compare_copies
            assert compare_copies(returned_outputs['filtered'], true_outputs['filtered']), 'Your output does not match the expected output.'
        ### end check_matches_ex3
        check_matches_helper(self.returned_output_vars, self.true_output_vars)

class Tester_ex4(ExerciseTester):
    def __init__(self, key=b'sIRWMgIhwENImJyOel3HWJDMr0VbXzfbq-uwgd09VFs=',  path='resource/asnlib/publicdata/', prevent_mod=True, tc_path=None):
        super().__init__(prevent_mod, tc_path)
        import pickle
        from cryptography.fernet import Fernet
        fernet = Fernet(key)
        try:
            with open(path + 'tc_ex4.pkl', 'rb') as fin:
                self.cases = pickle.loads(fernet.decrypt(fin.read()))
        except FileNotFoundError:
            print('file not found - Tester_ex4 may not work as expected')

    def build_vars(self):
        ### begin build_vars_ex4
        ### define build_vars_helper(cases)
        def build_vars_helper(cases):
            from random import choice
            case = choice(cases)
            input_vars = {'data': case['data'], 'key': case['key']}
            true_output_vars = {'summary': case['summary']}
            return input_vars, true_output_vars
           
        ### end build_vars_ex4
        self.input_vars, self.true_output_vars = build_vars_helper(self.cases)

    def run_func(self, func):
        ### begin run_func_ex4
        ### define run_func_helper(func, inputs)
        def run_func_helper(func, inputs):
            return {'summary': func (**inputs)}
        ### end run_func_ex4
        self.returned_output_vars = run_func_helper(func, self.input_vars)

    def check_type(self):
        ### begin check_type_ex4
        ### define check_type(outputs)
        def check_type_helper(outputs):
            top_o = outputs['summary']
            assert isinstance(top_o, dict), f'Summary should be instance of `dict`, but type{type(top_o)} was returned.'
            for k, v in top_o.items():
                assert type(k) is str, f'Keys should be of type `str`, but {type(k)} was returned.'
                assert isinstance(v, float), f'Values should be of type `float`, but {type(v)} was returned.'
        ### end check_type_ex4
        check_type_helper(self.returned_output_vars)


    def check_matches(self):
        ### begin check_matches_ex4
        ### Define check_matches_helper(returned_outputs, true_outputs)
        def check_matches_helper(returned_outputs, true_outputs):
            from tester_fw.test_utils import compare_copies
            assert compare_copies(returned_outputs, true_outputs), 'Your output did not match the expected output.'
        ### end check_matches_ex4
        check_matches_helper(self.returned_output_vars, self.true_output_vars)

class Tester_ex5(ExerciseTester):
    def __init__(self, key=b'sIRWMgIhwENImJyOel3HWJDMr0VbXzfbq-uwgd09VFs=',  path='resource/asnlib/publicdata/', prevent_mod=True, tc_path=None):
        super().__init__(prevent_mod, tc_path)
        import pickle
        from cryptography.fernet import Fernet
        fernet = Fernet(key)
        try:
            with open(path + 'tc_ex5.pkl', 'rb') as fin:
                self.cases = pickle.loads(fernet.decrypt(fin.read()))
        except FileNotFoundError:
            print('file not found - Tester_ex5 may not work as expected')

    def build_vars(self):
        ### begin build_vars_ex5
        ### define build_vars_helper(cases)
        def build_vars_helper(cases):
            from random import choice
            case = choice(cases)
            input_names = ['data', 'keys']
            output_names = ['corr_dict']
            return {name: case[name] for name in input_names}, {name: case[name] for name in output_names}
        ### end build_vars_ex5
        self.input_vars, self.true_output_vars = build_vars_helper(self.cases)

    def run_func(self, func):
        ### begin run_func_ex5
        ### define run_func_helper(func, inputs)
        def run_func_helper(func, inputs):
            output_names = ['corr_dict']
            outputs = func(**inputs)
            return {name: outputs for i, name in enumerate(output_names)}
        ### end run_func_ex5
        self.returned_output_vars = run_func_helper(func, self.input_vars)

    def check_type(self):
        ### begin check_type_ex5
        ### define check_type(outputs)
        def check_type_helper(outputs):
            o = outputs['corr_dict']
            assert isinstance(o, dict), f'`corr_dict` must be an instance of `dict`, but {type(o)} was returned.'
            for k, v in o.items():
                assert isinstance(k, str), f'keys should be `str`, but {type(k)} was returned.'
                assert isinstance(v, dict), f'values at the first level should be `dict`, not {type(v)}'
                for k_, v_ in v.items():
                    assert isinstance(k_, str), f'keys should be `str`, but {type(k_)} was returned.'
                    assert isinstance(v_, float), f'values at the second level should be `float`, not {type(v_)}'
        ### end check_type_ex5
        check_type_helper(self.returned_output_vars)


    def check_matches(self):
        ### begin check_matches_ex5
        ### Define check_matches_helper(returned_outputs, true_outputs)
        def check_matches_helper(returned_outputs, true_outputs):
            from tester_fw.test_utils import compare_copies
            assert compare_copies(returned_outputs, true_outputs), 'Returned output did not match expected output'
        ### end check_matches_ex5
        check_matches_helper(self.returned_output_vars, self.true_output_vars)

class Tester_ex6(ExerciseTester):
    def __init__(self, key=b'sIRWMgIhwENImJyOel3HWJDMr0VbXzfbq-uwgd09VFs=',  path='resource/asnlib/publicdata/', prevent_mod=True, tc_path=None):
        super().__init__(prevent_mod, tc_path)
        import pickle
        from cryptography.fernet import Fernet
        fernet = Fernet(key)
        try:
            with open(path + 'tc_ex6.pkl', 'rb') as fin:
                self.cases = pickle.loads(fernet.decrypt(fin.read()))
        except FileNotFoundError:
            print('file not found - Tester_ex6 may not work as expected')

    def build_vars(self):
        ### begin build_vars_ex6
        ### define build_vars_helper(cases)
        def build_vars_helper(cases):
            from random import choice
            case = choice(cases)
            input_vars = {'data': case['data'], 'n': case['n']}
            true_output_vars = {'leaders': case['leaders']}
            return input_vars, true_output_vars
        ### end build_vars_ex6
        self.input_vars, self.true_output_vars = build_vars_helper(self.cases)

    def run_func(self, func):
        ### begin run_func_ex6
        ### define run_func_helper(func, inputs)
        def run_func_helper(func, inputs):
            return {'leaders': func(**inputs)}
        ### end run_func_ex6
        self.returned_output_vars = run_func_helper(func, self.input_vars)

    def check_type(self):
        ### begin check_type_ex6
        ### define check_type(outputs)
        def check_type_helper(outputs):
            o = outputs['leaders']
            assert isinstance(o, dict), f'Output is required to be an instance of `dict`, {type(o)} was returned instead.'
            for k, v in o.items():
                assert isinstance(k, str), f'Output keys must be `str`, but {type(k)} was returned.'
                assert isinstance(v, list), f'Output values must be `list`, but {type(v)} was returned.'
                for li in v:
                    assert isinstance(li, str), f'Ingredient names must be `str`, but {type(li)} was returned.'
        ### end check_type_ex6
        check_type_helper(self.returned_output_vars)


    def check_matches(self):
        ### begin check_matches_ex6
        ### Define check_matches_helper(returned_outputs, true_outputs)
        def check_matches_helper(returned_outputs, true_outputs):
            from tester_fw.test_utils import compare_copies
            assert compare_copies(returned_outputs, true_outputs), 'Returned output does not match expected output.'
        ### end check_matches_ex6
        check_matches_helper(self.returned_output_vars, self.true_output_vars)














































































