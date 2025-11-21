class CI_CD:
    def output(self) -> str:
        return 'Running workflow manually'
    
instance = CI_CD()
print(instance.output())
