

class Solution(object):
    
    def getAllElements(self, root1, root2):
       
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        
        """
        
        self.traversal = []
        self.traverse(root1)
        self.traverse(root2)
        
        self.mergeSort(self.traversal)
        
        return self.traversal
    
    def traverse(self, node):
            
        if not node:
            return
        
        self.traverse(node.left)
        self.traversal.append(node.val)
        self.traverse(node.right)
        
 
    def mergeSort(self, lista):  
        

        
        if len(lista) >  1:

            meio = len(lista) // 2
            esquerdo = lista[:meio]
            direito = lista[meio:]
            
            lado_direito = Solution() #chamo a classe
            lado_direito.mergeSort(direito) #chamo a função
            
            lado_esquerdo = Solution()
            lado_esquerdo.mergeSort(esquerdo) #pressupõe que as lista já estão ordenadas
            

            i = 0
            j = 0
            k = 0
        
            while i < len(esquerdo) and j < len(direito):
                if esquerdo[i] < direito[j]:
                    lista[k] = esquerdo[i]
                    i = i + 1
                else:
                    lista[k] = direito[j]
                    j = j + 1
                k = k + 1
                
            while i < len(esquerdo):
                
                    lista[k] = esquerdo[i]
                    i = i + 1
                    k = k + 1
                    
            while j < len(direito):
                
                    lista[k] = direito[j]
                    j = j + 1
                    k = k + 1

              
        return lista
            

  
   
        
            
def main():
    
    root1 = [2,1,4]
    root2 = [1,0,3]

    print("Teste 1")
     
    s = Solution() 

    print(s.getAllElements(root1,root2)) #[0,1,1,2,3,4]
    
    root3 = [0,-10,10]
    root4 = [5,1,7,0,2]

    print("Teste 2")
     
    r = Solution() 

    print(r.getAllElements(root3,root4)) #[-10,0,0,1,2,5,7,10]
    
    root5 = []
    root6 = [5,1,7,0,2]

    print("Teste 3")
     
    t = Solution() 

    print(t.getAllElements(root5,root6)) #[0,1,2,5,7]
    
    root7 = [0, -10, 10]
    root8 = []

    print("Teste 4")
     
    u = Solution() 

    print(u.getAllElements(root7,root8)) #[-10,0,10]
    
 
    root9 = [1, None ,8]
    root10 = [1,1,8,8]

    print("Teste 5")
     
    v = Solution() 

    print(v.getAllElements(root9,root10)) #[0,1,1,2,3,4]


    
#main()

