

const btnAll = document.querySelector('#btnAll');
const addListenerOnButtons = () => {
    // Function to filter the books based on the button which is clicked on
    // options are all, created, contributed
    const bookAll = document.querySelectorAll('.book');
    const bookContributor = document.querySelectorAll('[data-book="contributor"]');
    const bookCreator = document.querySelector('[data-book="creator"]');
    const bookVisitor = document.querySelector('[data-book="visitor"]');
    
    
    const btnContributor = document.querySelector('#btnContributor');
    const btnCreator = document.querySelector('#btnCreator');

    // Button All
    btnAll.addEventListener('click', (e)=>{
        // if all is active
        btnAll.classList.toggle('book__button--active');
        if (btnAll.classList.contains('book__button--active')){
            // display all books
            bookAll.forEach((book) => book.classList.remove('hidden'));
            // deactivate buttons for created and contributed 
            btnContributor.classList.remove('book__button--active');
            btnCreator.classList.remove('book__button--active');
        } else{
            bookAll.forEach((book) => book.classList.add('hidden'));
        }
        
        
    });

    // Button Contributor
    btnContributor.addEventListener('click', (e)=>{
        btnContributor.classList.toggle('book__button--active');
        // if the button Contributed is active
        if (btnContributor.classList.contains('book__button--active')){
            // display all contributed books
            if(bookContributor !=null ){
                if (Array.isArray(bookCreator)){
                    bookContributor.forEach((book) => book.classList.remove('hidden'));
                }else{
                    if (bookContributor.classList != null ){
                        bookContributor.classList.remove('hidden'); 
                    }
                }
            }else{
                bookAll.forEach((book) => book.classList.add('hidden'));
            }
            
            
            if (bookCreator != null){
                // hide creator
                if(Array.isArray(bookCreator)){
                    bookCreator.forEach((book) => book.classList.add('hidden'));
                }else{
                    if (! bookCreator.classList.contains('hidden')){
                        bookCreator.classList.add('hidden');
                    }
                    
                }
                
            }
            if (bookVisitor != null){
               // hide visitor
                if(Array.isArray(bookVisitor)){
                    bookVisitor.forEach((book) => book.classList.add('hidden'));
                }else{
                    if (! bookVisitor.classList.contains('hidden')){
                        bookVisitor.classList.add('hidden');
                    }
                    
                }                
            }
            
        }else{
            // show all
            bookAll.forEach((book) => book.classList.remove('hidden'));
        }
        

    });
    // Button Creator
    btnCreator.addEventListener('click', (e)=>{
        btnCreator.classList.toggle('book__button--active');
        // if the button Creator is active
        if (btnCreator.classList.contains('book__button--active')){
            // display all creator books
            if (bookCreator != null){
                if (Array.isArray(bookCreator)){
                    bookCreator.forEach((book) => book.classList.remove('hidden'));
                }else{
                    if(bookCreator.classList.contains('hidden')){
                        bookCreator.classList.remove('hidden');
                    }
                }
            }else{
                bookAll.forEach((book) => book.classList.add('hidden'));
            }
            
            if (bookContributor != null){
                // hide contributor
                if (Array.isArray(bookContributor)){
                    bookContributor.forEach((book) => book.classList.add('hidden'));
                }else{
                    if (bookContributor.classList != null){
                        bookContributor.classList.add('hidden');
                    }
                }  
            }
            if (bookVisitor != null){
                // hide visitor
                if(Array.isArray(bookVisitor)){
                    bookVisitor.forEach((book) => book.classList.add('hidden'));
                }else{
                    if (bookVisitor.classList != null){
                        bookVisitor.classList.add('hidden');
                    }
                    
                }                
            }
            
        }else{
            //show all
            bookAll.forEach((book) => book.classList.remove('hidden'));
        }

    });
};

if (btnAll != null){
    addListenerOnButtons();
}
