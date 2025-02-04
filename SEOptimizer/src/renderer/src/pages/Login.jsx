import logo from './file-text-fill.svg'
import eye from './eye-fill.svg'
import {useState} from "react"
const Login = () => {
    const [showPassword, toggleShowPassword] = useState(false);
    const togglePasswordVisibility = () => {
        toggleShowPassword(!showPassword ? true : false)
    }
    return (
        <>
            <div className="bg-blue-800 h-screen">
                <div className="grid grid-cols-2 p-36">
                    <div className="col-span-1 text-white">
                        <div className="flex items-center mt-24">
                            <img src={logo} alt="Placeholder brand icon for SEOptimizer" height="50px" width="50px" />
                            <h1 className="text-3xl"> SEOptimizer </h1>
                        </div>
                    </div>
                    <div className="col-span-1 text-white">
                        <div className="w-fill h-64 bg-blue-900 rounded-2xl border-b-4 border-black">
                            <form className="p-12">
                                <label htmlFor="username"> Username </label>
                                <input type="text" className="rounded-full bg-blue-950 pl-3 w-full" id="username" />
                                <label htmlFor="password"> Password </label>
                                <img src={eye} className="cursor-pointer absolute right-50 top-67 opacity-50" alt="symbol for showing password" onClick={() => togglePasswordVisibility()}/>
                                <input type={`${showPassword ? `text` : `password`}`} className="rounded-full bg-blue-950 pl-3 w-full" id="username" />
                                <div className="pt-2 focus:pt-4">
                                    <button className="bg-blue-700 p-1 rounded-full text-sm w-full cursor-pointer border-black border-b-4 focus:mt-2 focus:border-0"> Login </button>
                                </div>

                            </form>
                        </div>
                    </div>

                </div>
            </div>
        </>
    )
}

export default Login