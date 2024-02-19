import unittest
from context import utils
from utils import blockchain
from web3 import Web3 
import json

abi = json.loads(
    '[{"constant":true,"inputs":[{"name":"hash","type":"bytes32"}],"name":"return_hash","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"hash","type":"bytes32"}],"name":"add_hash","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"hash","type":"bytes32"}],"name":"check_existence","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]')
# bytecode="608060405234801561001057600080fd5b506040805190810160405280600581526020017f48656c6c6f0000000000000000000000000000000000000000000000000000008152506000908051906020019061005c929190610062565b50610107565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106100a357805160ff19168380011785556100d1565b828001600101855582156100d1579182015b828111156100d05782518255916020019190600101906100b5565b5b5090506100de91906100e2565b5090565b61010491905b808211156101005760008160009055506001016100e8565b5090565b90565b610469806101166000396000f3fe608060405260043610610051576000357c010000000000000000000000000000000000000000000000000000000090048063a413686214610056578063cfae32171461011e578063ef690cc0146101ae575b600080fd5b34801561006257600080fd5b5061011c6004803603602081101561007957600080fd5b810190808035906020019064010000000081111561009657600080fd5b8201836020820111156100a857600080fd5b803590602001918460018302840111640100000000831117156100ca57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f82011690508083019250505050505050919291929050505061023e565b005b34801561012a57600080fd5b50610133610258565b6040518080602001828103825283818151815260200191508051906020019080838360005b83811015610173578082015181840152602081019050610158565b50505050905090810190601f1680156101a05780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b3480156101ba57600080fd5b506101c36102fa565b6040518080602001828103825283818151815260200191508051906020019080838360005b838110156102035780820151818401526020810190506101e8565b50505050905090810190601f1680156102305780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b8060009080519060200190610254929190610398565b5050565b606060008054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156102f05780601f106102c5576101008083540402835291602001916102f0565b820191906000526020600020905b8154815290600101906020018083116102d357829003601f168201915b5050505050905090565b60008054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156103905780601f1061036557610100808354040283529160200191610390565b820191906000526020600020905b81548152906001019060200180831161037357829003601f168201915b505050505081565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106103d957805160ff1916838001178555610407565b82800160010185558215610407579182015b828111156104065782518255916020019190600101906103eb565b5b5090506104149190610418565b5090565b61043a91905b8082111561043657600081600090555060010161041e565b5090565b9056fea165627a7a723058209bbad9ff08417d7b4bcd33671b3433a7e1bbf5b00a650b67e064551df6452bf00029"
contract_address = "0x68C7375827709848F649C2996fC806d10D5514d6"
bytecode = "608060405260043610610051576000357c010000000000000000000000000000000000000000000000000000000090048063082e8a351461005657806366e34cf1146100a5578063af5135fd146100e0575b600080fd5b34801561006257600080fd5b5061008f6004803603602081101561007957600080fd5b8101908080359060200190929190505050610133565b6040518082815260200191505060405180910390f35b3480156100b157600080fd5b506100de600480360360208110156100c857600080fd5b810190808035906020019092919050505061021c565b005b3480156100ec57600080fd5b506101196004803603602081101561010357600080fd5b81019080803590602001909291905050506102c9565b604051808215151515815260200191505060405180910390f35b600061013e826102c9565b15156101b2576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252600e8152602001807f48617368206e6f7420666f756e6400000000000000000000000000000000000081525060200191505060405180910390fd5b6000809050600090505b6000805490508110156101fa57826000828154811015156101d957fe5b906000526020600020015414156101ef576101fa565b8060010190506101bc565b60008181548110151561020957fe5b9060005260206000200154915050919050565b610225816102c9565b15151561029a576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260138152602001807f4861736820616c7265616479206578697374730000000000000000000000000081525060200191505060405180910390fd5b600081908060018154018082558091505090600182039060005260206000200160009091929091909150555050565b60008060009050600090505b60008054905081101561031857826000828154811015156102f257fe5b9060005260206000200154141561030d57600191505061031e565b8060010190506102d5565b60009150505b91905056fea165627a7a7230582063e90a26304ade1370e61db112b52a7ea3c7bdc441f21b030adb7add5c05cfa00029"


class Blockchain_Tests(unittest.TestCase):

	def test_connect(self):
		b = blockchain.Blockchain(url="http://127.0.0.1:7545" ,abi=abi ,contract_address= contract_address)
		self.assertTrue(b.connect() , msg="Connection failed")
		
	def test_check_hash(self):
		hash = "0x1b16b1df538ba12dc3f97edbb85caa7050d46c148134290feba80f8236c83db9"
		b = blockchain.Blockchain(url="http://127.0.0.1:7545" ,abi= abi ,contract_address= contract_address)
		self.assertIsNotNone(b.check_hash(hash) , msg="Hash already exists/ error")

	def test_insert_hash(self):
		hash = "0x1b16b1df538ba12dc3f97edbb85caa7050d46c148134290feba80f8236c83db9"
		b = blockchain.Blockchain(url="http://127.0.0.1:7545" ,abi= abi ,contract_address= contract_address)
		self.assertIsNone(b.insert_hash(hash) ,msg="Error. Inserted hash even if it existed.")
		new_hash = "0x1b16b1df538ba12dc3f97edbb85caa7050d46c148134290feba80f8236c83db0"
		self.assertIsNotNone(b.insert_hash(new_hash) , msg="Insertion failed")

	def test_return_hash(self):
		hash = "0x1b16b1df538ba12dc3f97edbb85caa7050d46c148134290feba80f8236c83db9"
		b = blockchain.Blockchain(url="http://127.0.0.1:7545" ,abi= abi ,contract_address= contract_address)
		self.assertIsNone(b.return_hash(hash) , msg="Returned hash even it didn't exist. ")
		new_hash = "0x1b16b1df538ba12dc3f97edbb85caa7050d46c148134290feba80f8236c83db1"
		ret_hash = b.insert_hash(new_hash)

		self.assertEqual(new_hash,ret_hash , msg="Hashes not equal")		

if __name__ == "__main__":
	unittest.main()		
