import React, { useContext, useEffect } from "react";
import { Footer } from 'flowbite-react'

const Home = () => {
    return(
        <>
            <div className="relative overflow-hidden bg-white">
                <div className="pb-80 pt-16 sm:pb-40 sm:pt-24 lg:pb-48 lg:pt-40">
                    <div className="relative mx-auto max-w-7xl px-4 sm:static sm:px-6 lg:px-8">
                        <div className="sm:max-w-lg mt-10">
                        <h1 className="text-4xl font-bold tracking-tight text-pink-700 sm:text-4xl">
                            Woman can be everything !
                        </h1>
                        <p className="mt-4 text-xl text-gray-500">
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Morbi blandit cursus risus at ultrices.                        </p>
                        </div>
                    <div>
                        <div className="mt-10">
                        <div
                            aria-hidden="true"
                            className="pointer-events-none lg:absolute lg:inset-y-0 lg:mx-auto lg:w-full lg:max-w-7xl"
                        >
                            <div className="absolute transform sm:left-1/2 sm:top-0 sm:translate-x-8 lg:left-1/2 lg:top-1/2 lg:-translate-y-1/2 lg:translate-x-8">
                            <div className="flex items-center space-x-6 lg:space-x-8">
                                <div className="grid flex-shrink-0 grid-cols-1 gap-y-6 lg:gap-y-8">
                                <div className="h-64 w-44 overflow-hidden rounded-lg sm:opacity-0 lg:opacity-100">
                                    <img
                                    src="https://img.freepik.com/free-photo/lifestyle-business-people-using-laptop-computer-pink_1150-15547.jpg?w=900&t=st=1695182487~exp=1695183087~hmac=5e830b8d432baa9e99751a1be90361332ebf0ea5b76d1c2611f6b4e087926597"
                                    alt=""
                                    className="h-full w-full object-cover object-center"
                                    />
                                </div>
                                <div className="h-64 w-44 overflow-hidden rounded-lg">
                                    <img
                                    src="https://img.freepik.com/free-photo/asian-medical-doctor-woman-with-white-lab-coat-pink_1150-18679.jpg?w=360&t=st=1695193929~exp=1695194529~hmac=37e01c9a35c0b0875cd6641fbed6fe8d35e427813f964cf9443fb9db26f58a37"
                                    alt=""
                                    className="h-full w-full object-cover object-center"
                                    />
                                </div>
                                </div>
                                <div className="grid flex-shrink-0 grid-cols-1 gap-y-6 lg:gap-y-8">
                                <div className="h-64 w-44 overflow-hidden rounded-lg">
                                    <img
                                    src="https://cdn.media.amplience.net/s/hottopic/20507822_hi?$productMainDesktop$"
                                    alt=""
                                    className="h-full w-full object-cover object-center"
                                    />
                                </div>
                                <div className="h-64 w-44 overflow-hidden rounded-lg">
                                    <img
                                    src="https://img.freepik.com/free-photo/pretty-wonderful-woman-with-red-lips-fashionable-jacket-eyeglasses-poses-with-computer-tablet-isolated-pink-background_197531-18662.jpg?w=900&t=st=1695194310~exp=1695194910~hmac=5b45e3c543ace44de478f13d172de2369ea006fd68d59ff518a93f872ee1b628"
                                    alt=""
                                    className="h-full w-full object-cover object-center"
                                    />
                                </div>
                                <div className="h-64 w-44 overflow-hidden rounded-lg">
                                    <img
                                    src="https://img.freepik.com/free-photo/repair-concept-positive-woman-mechanic-wears-engineering-building-uniform-looks-happily-isolated-pink-wall-engineering-industrial-building-laborer-working-clothes_273609-48630.jpg?w=900&t=st=1695194419~exp=1695195019~hmac=3cedbe597a96fc4f8e19949017f86858176ebbfe88b0125e4217ad3757f41b74"
                                    alt=""
                                    className="h-full w-full object-cover object-center"
                                    />
                                </div>
                                </div>
                                <div className="grid flex-shrink-0 grid-cols-1 gap-y-6 lg:gap-y-8">
                                <div className="h-64 w-44 overflow-hidden rounded-lg">
                                    <img
                                    src="https://img.freepik.com/free-photo/front-view-young-pretty-housewife-cape-with-spoons-pink-wall_140725-151989.jpg?w=900&t=st=1695194771~exp=1695195371~hmac=0c278ccbdfcfe5606f0aad8e0c65ee30fbed31f5e7268cbd5943df5649e204ec"
                                    alt=""
                                    className="h-full w-full object-cover object-center"
                                    />
                                </div>
                                <div className="h-64 w-44 overflow-hidden rounded-lg">
                                    <img
                                    src="https://img.freepik.com/free-photo/young-sporty-woman-headband-holding-two-air-tickets-soccer-ball-smiling-cheerfully-standing-pink-wall_141793-50222.jpg?w=900&t=st=1695195147~exp=1695195747~hmac=4964bf48889316f76d9e65e25aef3abbe86b8c282825315b1c130d902d840ba6"
                                    alt=""
                                    className="h-full w-full object-cover object-center"
                                    />
                                </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        <a
                            href="/job-vacancy"
                            className="inline-block rounded-md border border-transparent bg-pink-600 px-8 py-3 text-center font-medium text-white hover:bg-[#87CED0]"
                        >
                            Get Started
                        </a>
                        </div>
                    </div>
                    </div>
                </div>
            </div>



            <>
            <section className="relative isolate overflow-hidden bg-white px-6 py-24 sm:py-32 lg:px-8">
                <div className="absolute inset-0 -z-10 bg-[radial-gradient(45rem_50rem_at_top,theme(colors.indigo.100),white)] opacity-20" />
                <div className="absolute inset-y-0 right-1/2 -z-10 mr-16 w-[200%] origin-bottom-left skew-x-[-30deg] bg-white shadow-xl shadow-indigo-600/10 ring-1 ring-indigo-50 sm:mr-28 lg:mr-0 xl:mr-16 xl:origin-center" />
                <div className="mx-auto max-w-2xl lg:max-w-4xl">
                <img
                    className="mx-auto h-12"
                    src="https://tailwindui.com/img/logos/workcation-logo-indigo-600.svg"
                    alt=""
                />
                <figure className="mt-10">
                    <blockquote className="text-center text-xl font-semibold leading-8 text-gray-900 sm:text-2xl sm:leading-9">
                    <p>
                        “Lorem ipsum dolor sit amet consectetur adipisicing elit. Nemo
                        expedita voluptas culpa sapiente alias molestiae. Numquam corrupti
                        in laborum sed rerum et corporis.”
                    </p>
                    </blockquote>
                    <figcaption className="mt-10">
                    <img
                        className="mx-auto h-10 w-10 rounded-full"
                        src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
                        alt=""
                    />
                    <div className="mt-4 flex items-center justify-center space-x-3 text-base">
                        <div className="font-semibold text-gray-900">Judith Black</div>
                        <svg
                        viewBox="0 0 2 2"
                        width={3}
                        height={3}
                        aria-hidden="true"
                        className="fill-gray-900"
                        >
                        <circle cx={1} cy={1} r={1} />
                        </svg>
                        <div className="text-gray-600">CEO of Workcation</div>
                    </div>
                    </figcaption>
                </figure>
                </div>
            </section>
            </>




            <div class="flex-wrap items-center justify-center gap-8 text-center sm:flex">
                <div class="w-full px-4 py-4 mt-6 bg-white rounded-lg shadow-lg sm:w-1/2 md:w-1/2 lg:w-1/4 dark:bg-gray-800">
                    <div class="flex-shrink-0">
                        <div class="flex items-center justify-center w-12 h-12 mx-auto text-white bg-indigo-500 rounded-md">
                            <svg width="20" height="20" fill="currentColor" class="w-6 h-6" viewBox="0 0 1792 1792" xmlns="http://www.w3.org/2000/svg">
                                <path d="M491 1536l91-91-235-235-91 91v107h128v128h107zm523-928q0-22-22-22-10 0-17 7l-542 542q-7 7-7 17 0 22 22 22 10 0 17-7l542-542q7-7 7-17zm-54-192l416 416-832 832h-416v-416zm683 96q0 53-37 90l-166 166-416-416 166-165q36-38 90-38 53 0 91 38l235 234q37 39 37 91z">
                                </path>
                            </svg>
                        </div>
                    </div>
                    <h3 class="py-4 text-2xl font-semibold text-gray-700 sm:text-xl dark:text-white">
                        Website Design
                    </h3>
                    <p class="py-4 text-gray-500 text-md dark:text-gray-300">
                        Encompassing today’s website design technology to integrated and build solutions relevant to your business.
                    </p>
                </div>
                <div class="w-full px-4 py-4 mt-6 bg-white rounded-lg shadow-lg sm:w-1/2 md:w-1/2 lg:w-1/4 sm:mt-16 md:mt-20 lg:mt-24 dark:bg-gray-800">
                    <div class="flex-shrink-0">
                        <div class="flex items-center justify-center w-12 h-12 mx-auto text-white bg-indigo-500 rounded-md">
                            <svg width="20" height="20" fill="currentColor" class="w-6 h-6" viewBox="0 0 1792 1792" xmlns="http://www.w3.org/2000/svg">
                                <path d="M491 1536l91-91-235-235-91 91v107h128v128h107zm523-928q0-22-22-22-10 0-17 7l-542 542q-7 7-7 17 0 22 22 22 10 0 17-7l542-542q7-7 7-17zm-54-192l416 416-832 832h-416v-416zm683 96q0 53-37 90l-166 166-416-416 166-165q36-38 90-38 53 0 91 38l235 234q37 39 37 91z">
                                </path>
                            </svg>
                        </div>
                    </div>
                    <h3 class="py-4 text-2xl font-semibold text-gray-700 sm:text-xl dark:text-white">
                        Branding
                    </h3>
                    <p class="py-4 text-gray-500 text-md dark:text-gray-300">
                        Share relevant, engaging, and inspirational brand messages to create a connection with your audience.
                    </p>
                </div>
                <div class="w-full px-4 py-4 mt-6 bg-white rounded-lg shadow-lg sm:w-1/2 md:w-1/2 lg:w-1/4 dark:bg-gray-800">
                    <div class="flex-shrink-0">
                        <div class="flex items-center justify-center w-12 h-12 mx-auto text-white bg-indigo-500 rounded-md">
                            <svg width="20" height="20" fill="currentColor" class="w-6 h-6" viewBox="0 0 1792 1792" xmlns="http://www.w3.org/2000/svg">
                                <path d="M491 1536l91-91-235-235-91 91v107h128v128h107zm523-928q0-22-22-22-10 0-17 7l-542 542q-7 7-7 17 0 22 22 22 10 0 17-7l542-542q7-7 7-17zm-54-192l416 416-832 832h-416v-416zm683 96q0 53-37 90l-166 166-416-416 166-165q36-38 90-38 53 0 91 38l235 234q37 39 37 91z">
                                </path>
                            </svg>
                        </div>
                    </div>
                    <h3 class="py-4 text-2xl font-semibold text-gray-700 sm:text-xl dark:text-white">
                        SEO Marketing
                    </h3>
                    <p class="py-4 text-gray-500 text-md dark:text-gray-300">
                        Let us help you level up your search engine game, explore our solutions for digital marketing for your business.
                    </p>
                </div>
            </div>


            <div className="bg-pink-200 py-16 sm:py-25">
                <div className="mx-auto max-w-7xl px-6 lg:px-8">
                    <h2 className="text-center text-lg font-semibold leading-8 text-pink-700">
                        Trusted by the world’s most innovative teams
                    </h2>
                    <div className="mx-auto mt-5 grid max-w-lg grid-cols-4 items-center gap-x-8 gap-y-10 sm:max-w-xl sm:grid-cols-6 sm:gap-x-10 lg:mx-0 lg:max-w-none lg:grid-cols-5">
                    <img
                        className="col-span-2 max-h-12 w-full object-contain lg:col-span-1"
                        src="https://1.bp.blogspot.com/-GSGIvKPaFpQ/YIJv46dHKpI/AAAAAAAACj8/Hk8UOIt5NgEk29fqHsPGJheVi8dUHP83wCNcBGAsYHQ/w1200-h630-p-k-no-nu/Shopee.png"
                        alt="Shopee"
                        width={158}
                        height={48}
                    />
                    <img
                        className="col-span-2 max-h-12 w-full object-contain lg:col-span-1"
                        src="https://tailwindui.com/img/logos/158x48/reform-logo-gray-900.svg"
                        alt="Reform"
                        width={158}
                        height={48}
                    />
                    <img
                        className="col-span-2 max-h-12 w-full object-contain lg:col-span-1"
                        src="https://tailwindui.com/img/logos/158x48/tuple-logo-gray-900.svg"
                        alt="Tuple"
                        width={158}
                        height={48}
                    />
                    <img
                        className="col-span-2 max-h-12 w-full object-contain sm:col-start-2 lg:col-span-1"
                        src="https://tailwindui.com/img/logos/158x48/savvycal-logo-gray-900.svg"
                        alt="SavvyCal"
                        width={158}
                        height={48}
                    />
                    <img
                        className="col-span-2 col-start-2 max-h-12 w-full object-contain sm:col-start-auto lg:col-span-1"
                        src="https://tailwindui.com/img/logos/158x48/statamic-logo-gray-900.svg"
                        alt="Statamic"
                        width={158}
                        height={48}
                    />
                    </div>
                </div>
            </div>



            <footer className="footer p-10 bg-base-300 text-base-content">
  <nav>
    <header className="footer-title">Services</header> 
    <a className="link link-hover">Branding</a> 
    <a className="link link-hover">Design</a> 
    <a className="link link-hover">Marketing</a> 
    <a className="link link-hover">Advertisement</a>
  </nav> 
  <nav>
    <header className="footer-title">Company</header> 
    <a className="link link-hover">About us</a> 
    <a className="link link-hover">Contact</a> 
    <a className="link link-hover">Jobs</a> 
    <a className="link link-hover">Press kit</a>
  </nav> 
  <nav>
    <header className="footer-title">Social</header> 
    <div className="grid grid-flow-col gap-4">
      <a><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" className="fill-current"><path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"></path></svg></a>
      <a><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" className="fill-current"><path d="M19.615 3.184c-3.604-.246-11.631-.245-15.23 0-3.897.266-4.356 2.62-4.385 8.816.029 6.185.484 8.549 4.385 8.816 3.6.245 11.626.246 15.23 0 3.897-.266 4.356-2.62 4.385-8.816-.029-6.185-.484-8.549-4.385-8.816zm-10.615 12.816v-8l8 3.993-8 4.007z"></path></svg></a>
      <a><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" className="fill-current"><path d="M9 8h-3v4h3v12h5v-12h3.642l.358-4h-4v-1.667c0-.955.192-1.333 1.115-1.333h2.885v-5h-3.808c-3.596 0-5.192 1.583-5.192 4.615v3.385z"></path></svg></a>
    </div>
  </nav>
</footer>

        </>
    )
}

export default Home