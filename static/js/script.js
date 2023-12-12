const addListenerOnButtons = () => {
    const bookAll = document.querySelectorAll('.book');
    const bookContributor = document.querySelectorAll('[data-book="contributor"]');
    const bookCreator = document.querySelector('[data-book="creator"]');
    const bookVisitor = document.querySelector('[data-book="visitor"]');

    console.log(bookContributor)
    
    const btnAll = document.querySelector('#btnAll');
    const btnContributor = document.querySelector('#btnContributor');
    const btnCreator = document.querySelector('#btnCreator');

    // Button All
    btnAll.classList.add('book__button--active');
    btnAll.addEventListener('click', (e)=>{
        console.log('al')
        bookAll.forEach((book) => book.classList.toggle('hidden'));
        btnAll.classList.toggle('book__button--active');
    });

    // Button Contributor
    btnContributor.addEventListener('click', (e)=>{
        if (bookContributor != null){
            bookVisitor.classList.toggle('hidden');
            bookVisitor.forEach((book) => book.classList.toggle('hidden'));
            
            if (btnAll.classList.contains('book__button--active')){
                btnAll.classList.remove('book__button--active');
                btnContributor.classList.toggle('book__button--active');
                
            }else{
                btnAll.classList.add('book__button--active')
                btnContributor.classList.toggle('book__button--active');
            }
        }
        

    });
    // Button CCreator
    btnCreator.addEventListener('click', (e)=>{

        if (bookCreator != null ){
            bookCreator.forEach((book) => book.classList.toggle('hidden'));
        
            bookCreator.classList.toggle('book__button--active');
            if (btnAll.classList.contains('book__button--active')){
                btnAll.classList.remove('book__button--active');
            }else{
                btnAll.classList.add('book__button--active')
            }
        }

    });
};

addListenerOnButtons();