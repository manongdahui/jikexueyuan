namespace py jikexueyuan

struct RecomRequest{
  1:required string userid;
  2:required list<string> his_list;
  3:i32 pageid;
  4:i32 areaid;
  5:required i32 num;
}

struct RecomResponse{
  1:list<string> recom_list;
}


service RecomService{
RecomResponse getRecomResponse(1:RecomRequest para)
}
