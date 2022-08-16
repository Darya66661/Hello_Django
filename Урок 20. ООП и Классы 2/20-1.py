class phone:
    @staticmethod
    def model_hash(model):
        if model == '1785':
            return 34565
        elif model == 'K498':
            return  45567
        else:
            return None
print(phone.model_hash('1785'))



