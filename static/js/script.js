const addListenerOnButtons = () => {
    let bookAll = document.querySelectorAll('.book');
    let bookContributor = document.querySelectorAll('[data-book="contributor"]');
    let bookCreator = document.querySelector('[data-book="creator"]');
    let bookVisitor = document.querySelector('[data-book="visitor"]');
    
    const btnAll = document.querySelector('#btnAll');
    const btnContributor = document.querySelector('#btnContributor');
    const btnCreator = document.querySelector('#btnCreator');

    console.log(bookCreator == null)

    // Button All
    btnAll.classList.add('book__button--active')
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
            console.log('active')
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
                console.log('hide creator')
                if(Array.isArray(bookCreator)){
                    bookCreator.forEach((book) => book.classList.add('hidden'));
                }else{
                    if (! bookCreator.classList.contains('hidden')){
                        bookCreator.classList.add('hidden');
                    }
                    
                }
                
            }
            if (bookVisitor != null){
                console.log('hide Visitor')
                if(Array.isArray(bookVisitor)){
                    bookVisitor.forEach((book) => book.classList.add('hidden'));
                }else{
                    if (! bookVisitor.classList.contains('hidden')){
                        bookVisitor.classList.add('hidden');
                    }
                    
                }                
            }
            
        }else{
            console.log('deactivate')
            bookAll.forEach((book) => book.classList.remove('hidden'));
        }
        

    });
    // Button Creator
    btnCreator.addEventListener('click', (e)=>{
        btnCreator.classList.toggle('book__button--active');
        // if the button Creator is active
        if (btnCreator.classList.contains('book__button--active')){
            console.log('active')
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
                console.log('hide contribution')
                if (Array.isArray(bookContributor)){
                    bookContributor.forEach((book) => book.classList.add('hidden'));
                }else{
                    if (bookContributor.classList != null){
                        bookContributor.classList.add('hidden');
                    }
                }  
            }
            if (bookVisitor != null){
                console.log('hide Visitor')
                if(Array.isArray(bookVisitor)){
                    bookVisitor.forEach((book) => book.classList.add('hidden'));
                }else{
                    if (bookVisitor.classList != null){
                        bookVisitor.classList.add('hidden');
                    }
                    
                }                
            }
            
        }else{
            console.log('deactivate')
            bookAll.forEach((book) => book.classList.remove('hidden'));
        }

    });
};

addListenerOnButtons();