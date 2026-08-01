class Node{
    int key;
    int value;
    Node prev;
    Node next;

    public Node(int key,int value)
    {
        this.key=key;
        this.value=value;
        this.prev=null;
        this.next=null;
    }
}

class LRUCache {
    private int cap;
    private HashMap<Integer, Node> cache;
    private Node right;
    private Node left;
    //private void remove(Node node);
    //private void insert(Node node);

    public LRUCache(int capacity) {
        this.cap = capacity;
        this.cache = new HashMap<>();
        this.left = new Node(0,0);
        this.right = new Node(0,0);
        this.left.next=this.right;
        this.right.prev=this.left;

    }

    private void remove(Node node)
    {
        Node prv=node.prev;
        Node nxt=node.next;
        prv.next=nxt;
        nxt.prev = prv;
    }

    private void insert(Node node)
    {
        Node prv=this.right.prev;
        prv.next=node;
        node.prev=prv;
        node.next=this.right;
        this.right.prev=node;
    }
    
    public int get(int key) {
        if(cache.containsKey(key))
        {
            Node node = cache.get(key);
            remove(node);
            insert(node);
            return node.value;
        }
        return -1;
    }
    
    public void put(int key, int value) {
        if(cache.containsKey(key))
        {
            Node node=cache.get(key); 
            remove(node);
        }
        Node node = new Node(key,value);
        cache.put(key,node);
        insert(node);

        if (cache.size() > cap)
        {
            Node lru = this.left.next;
            remove(lru);
            cache.remove(lru.key);
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */